import pandas as pd;
from sklearn.model_selection import train_test_split
from tools.Sort import Sort
from tools.RecordID import RecordID


class OverSample:
    def __init__(self,yxdb_tool=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        if config:
            self.config = config
        elif yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        elif json:
            self.load_json(json);
        elif kwargs:
            self.load_json(kwargs);

    def load_json(self,json):
        c = self.config;

    def load_yxdb_tool(self,tool,execute=True):
        c = self.config;
        xml = tool.xml;
        values = {v.get("name"):v.text for v in xml.find(".//Configuration")}

        c.field = values["Selected_Field"]
        c.value = values["Oversample_Value"]
        c.sample = int(values["Desired_Pct"])

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

    class Config:
        def __init__(
            self
        ):
            self.field = None;
            self.value = None;
            self.sample = 50;

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
