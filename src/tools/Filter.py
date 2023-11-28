import pandas as pd;
from tools.Formula import Functions

class Filter:
    def __init__(self,yxdb_tool=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        self.true = None;
        self.false = None;
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
        xml = tool.xml

        if  xml.find(".//Configuration//Mode").text != "Custom":
            raise Exception("Filter tool must use custom expression! Simply open the WF and change the filter type to a custom expression.")

        c.expression = xml.find(".//Configuration//Expression").text

        if execute:
            df = tool.get_input("Input")
            out = self.execute(df)
            tool.data["True"] = out.true
            tool.data["False"] = out.false

    def applier(self,series):
        c = self.config
        return eval(c.expression)

    def execute(self,input_datasource):
        c = self.config;
        new_df = input_datasource.copy()
        if isinstance(c.expression,str):
            c.expression = Functions.parse_formula(c.expression,column_names=new_df.columns,df_name='series')

        mask = new_df.apply(self.applier,axis=1)

        self.true = new_df[mask].reset_index(drop = True)
        self.false = new_df[~mask].reset_index(drop = True)
        return self

    class Config:
        def __init__(
            self
        ):
            self.expression = "True"

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
