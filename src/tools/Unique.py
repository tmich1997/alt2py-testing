import pandas as pd;

class Unique:
    def __init__(self,yxdb_tool=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        self.unique = None;
        self.duplicates = None;

        if config:
            self.config = config
        elif yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        elif json:
            self.load_json(json);
        elif kwargs:
            self.load_json(kwargs);

    def load_yxdb_tool(self,xml):
        c = self.config;

        c.fields = [f.get("field") for f in xml.find(".//Configuration//UniqueFields")]

        if execute:
            df = tool.get_input("Input")
            out = Unique(xml=tool.xml).execute(df)

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
