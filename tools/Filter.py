import pandas as pd;
from tools.Formula import Functions

class Filter:
    def __init__(self,xml=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);

        self.true = None;
        self.false = None;

    def load_xml(self,xml):
        c = self.config;

        if  xml.find(".//Configuration//Mode").text != "Custom":
            raise Exception("Filter tool must use custom expression! Simply open the WF and change the filter type to a custom expression.")
        c.expression = xml.find(".//Configuration//Expression").text

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
