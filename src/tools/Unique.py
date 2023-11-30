from .Config import Config;
import pandas as pd;


INPUT_CONSTRAINTS = [
    {
        "name":"fields",
        "required":True,
        "type":list,
        "sub_type":str,
        "field":True
    }
]

class Unique:
    def __init__(self,yxdb_tool=None,**kwargs):
        # LOAD DEFAULTS
        self.config = Config(INPUT_CONSTRAINTS);
        self.unique = None;
        self.duplicates = None;
        if yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        else:
            self.config.load(kwargs)

    def load_yxdb_tool(self,tool,execute=True):
        xml = tool.xml;
        kwargs = {};
        kwargs['fields'] = [f.get("field") for f in xml.find(".//Configuration//UniqueFields")]
        self.config.load(kwargs)

        if execute:
            df = tool.get_input("Input")
            out = self.execute(df)

            tool.data["Unique"] = out.unique
            tool.data["Duplicates"] = out.duplicates

    def execute(self,input_datasource):
        c = self.config;
        new_df = input_datasource.copy()
        mask = new_df.duplicated(subset=c.fields, keep='first')
        self.unique = new_df[~mask].reset_index(drop = True)
        self.duplicates = new_df[mask].reset_index(drop = True)
        return self

    class Config:
        def __init__(
            self
        ):
            self.fields=[];

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
