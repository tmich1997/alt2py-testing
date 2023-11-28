import pandas as pd
from tools.Select import dtype_map

class RecordID:
    def __init__(self,yxdb_tool=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        if config:
            self.config = config
        elif yxdb_tool:
            self.load_yxdb_tool(yxdb_tool);
        elif json:
            self.load_json(json);
        elif kwargs:
            self.load_json(kwargs);

    def load_json(self,kwargs):
        c = self.config;

        c.field = kwargs["field"] if "field" in kwargs else c.field
        c.start = kwargs["start"] if "start" in kwargs else c.start
        c.type = kwargs["type"] if "type" in kwargs else c.type
        c.size = kwargs["size"] if "size" in kwargs else c.size
        c.position = kwargs["position"] if "position" in kwargs else c.position


    def load_yxdb_tool(self,xml):
        c = self.config;

        c.field = xml.find(".//Configuration//FieldName").text
        c.start = int(xml.find(".//Configuration//StartValue").text)
        c.type = dtype_map[xml.find(".//Configuration//FieldType").text]
        c.size = int(xml.find(".//Configuration//FieldSize").text)
        c.position = True if xml.find(".//Configuration//Position").text=="0" else False;

        if execute:
            df = tool.get_input("Input")
            next_df = RecordID(xml=tool.xml).execute(df)
            tool.data["Output"] = next_df

    def execute(self,input_datasource):
        c = self.config

        new_df = input_datasource.copy();
        new_df[c.field] = range(c.start,c.start + len(new_df))
        new_df[c.field] = new_df[c.field].astype(c.type)

        if c.position:
            new_df = new_df.loc[:, [c.field]+input_datasource.columns.tolist()]
        if c.type=="string":
            new_df[c.field] = new_df[c.field].str.zfill(c.size)

        return new_df

    class Config:
        def __init__(
            self
        ):
            self.field=None
            self.start=1
            self.type=dtype_map["Int64"]
            self.size=None
            self.position=False

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
