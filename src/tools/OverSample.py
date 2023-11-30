from .Config import Config;
import pandas as pd;
from sklearn.model_selection import train_test_split
from tools.Sort import Sort
from tools.RecordID import RecordID

INPUT_CONSTRAINTS = [
    {
        "name":"field",
        "required":True,
        "type":str,
        "field":True
    },{
        "name":"value",
        "required":True
    },{
        "name":"sample",
        "required":False,
        "type":int
    }
]

class OverSample:
    def __init__(self,yxdb_tool=None,**kwargs):
        # LOAD DEFAULTS
        self.config = Config(INPUT_CONSTRAINTS);
        if yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        else:
            self.config.load(kwargs)


    def load_json(self,json):
        c = self.config;

    def load_yxdb_tool(self,tool,execute=True):
        kwargs = {}
        xml = tool.xml;
        values = {v.get("name"):v.text for v in xml.find(".//Configuration")}

        kwargs["field"] = values["Selected_Field"]
        kwargs["value"] = values["Oversample_Value"]
        kwargs["sample"] = int(values["Desired_Pct"])
        self.config.load(kwargs)
        if execute:
            df = tool.get_input("Input")
            next_df = self.execute(df)
            tool.data["Output"] = next_df

    def execute(self,input_datasource):
        c = self.config;

        new_df = RecordID(field="__record_id__").execute(input_datasource.copy())

        over_sample_df = new_df[new_df[c.field] == c.value]
        under_sample_df = new_df[new_df[c.field] != c.value]

        pre_pct = len(over_sample_df) / len(new_df)

        if pre_pct < c.sample/100:
            #we only care if the field is underrepresented relative to the goal sample rates
            #take all of the over sample df and an amount of the under sample df that results in the goal sample rate.
            under_sample_amt = len(over_sample_df)*(100-c.sample)/c.sample

            keep, discard = train_test_split(under_sample_df, train_size=int(under_sample_amt))

            new_df = pd.concat([over_sample_df,keep])

            new_df = Sort(fields=["__record_id__"]).execute(new_df)
            new_df = new_df.drop("__record_id__", axis=1)
        else:
            return new_df

        return new_df.reset_index(drop=True)
