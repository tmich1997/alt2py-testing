import pandas as pd;

class Unique:
    def __init__(self,xml=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);

        self.unique = None;
        self.duplicates = None;

    def load_xml(self,xml):
        c = self.config;

        c.fields = [f.get("field") for f in xml.find(".//Configuration//UniqueFields")]

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
