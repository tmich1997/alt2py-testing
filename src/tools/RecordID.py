from .Config import Config;
import pandas as pd
from _utils import dtype_map

INPUT_CONSTRAINTS = [
    {
        "name":"field",
        "required":True,
        "type":str,
    },
    {
        "name":"start",
        "required":False,
        "default":1,
        "type":int
    },
    {
        "name":"type",
        "required":False,
        "type":str,
        "multi_choice":list(dtype_map.keys()),
        "default":"Int"
    },
    {
        "name":"size",
        "required":False,
        "type":str
    },
    {
        "name":"position_first",
        "required":False,
        "default":False,
        "type":bool
    },
]


class RecordID:
    def __init__(self,yxdb_tool=None,**kwargs):
        # LOAD DEFAULTS
        self.config = Config(INPUT_CONSTRAINTS);
        if yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        else:
            self.config.load(kwargs)


    def load_yxdb_tool(self,tool,execute=True):
        xml = tool.xml

        kwargs = {}
        kwargs["field"] = xml.find(".//Configuration//FieldName").text
        kwargs["start"] = int(xml.find(".//Configuration//StartValue").text)
        kwargs["type"] = xml.find(".//Configuration//FieldType").text
        kwargs["size"] = xml.find(".//Configuration//FieldSize").text
        kwargs["position_first"] = True if xml.find(".//Configuration//Position").text=="0" else False;

        self.config.load(kwargs)

        if execute:
            df = tool.get_input("Input")
            next_df = self.execute(df)
            tool.data["Output"] = next_df

    def execute(self,input_datasource):
        c = self.config

        new_df = input_datasource.copy();
        new_df[c.field] = range(c.start,c.start + len(new_df))
        new_df[c.field] = new_df[c.field].astype(dtype_map[c.type])

        if c.position_first:
            new_df = new_df.loc[:, [c.field]+input_datasource.columns.tolist()]
        if c.type=="String":
            new_df[c.field] = new_df[c.field].str.zfill(int(c.size))

        return new_df
