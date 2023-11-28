import pandas as pd;

class MultiFieldBin:
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

        field_statements = values["List Box (297)"].split(',')
        c.fields = [f.split("=")[0] for f in field_statements if f.split("=")[1]=="True"]
        c.mode = "count" if values["Radio Button (299)"]=="True" else "interval"#count
        c.bins = int(values["Numeric Up Down (298)"]) if values["Radio Button (299)"]=="True" else int(values["Numeric Up Down (300)"])
        c.suffix = "_Tile_Num"

        if execute:
            df = tool.get_input("Input")
            next_df = self.execute(df)
            tool.data["Output"] = next_df

    def execute(self,input_datasource):
        c = self.config;

        new_df = input_datasource.copy()
        if c.mode == "count":
            for f in c.fields:
                new_df[c.prefix + f + c.suffix], bins = pd.qcut(new_df[f], q=c.bins, labels=range(c.bins,0,-1),retbins=True)
                print(bins)
        elif c.mode == "interval":
            for f in c.fields:
                new_df[c.prefix + f + c.suffix] = pd.cut(new_df[f], bins=c.bins, labels=range(1,c.bins+1),precision=10)
        else:
            raise Exception("mode must be set to 'count' or 'interval'.")

        return new_df

    class Config:
        def __init__(
            self
        ):
            self.fields = []
            self.mode = "count" # count|interval
            self.bins = 2
            self.prefix = ''
            self.suffix = ''

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
