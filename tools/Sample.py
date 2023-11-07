import pandas as pd
from sklearn.model_selection import train_test_split

class Sample:
    def __init__(self,xml=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);
        elif kwargs:
            self.load_json(kwargs);


    def load_json(self,json):
        c = self.config;

        c.train = json["train"]
        c.seed = json["seed"] if "seed" in json else None;

    def load_xml(self,xml):
        c = self.config;

        values = {v.get("name"):int(v.text) for v in xml.find(".//Configuration")}

        c.train = values["estimation pct"]/100
        c.validate = values["validation pct"]/100 #(100 - values["estimation pct"])
        c.seed = values["rand seed"]

    def execute(self,input_datasource):
        c = self.config;

        new_df = input_datasource.copy();

        if c.train <= 1:
            c.train = round(c.train*len(new_df))
            c.validate = round(c.validate*len(new_df))
        if c.validate == 0:
            c.validate = len(new_df) - c.train

        temp, train = train_test_split(new_df, test_size=c.train, random_state=c.seed,shuffle=c.shuffle)
        if len(temp)==c.validate:
            validate=temp
            hold = new_df.head(0);
        else:
            hold, validate = train_test_split(temp, test_size=c.validate, random_state=c.seed,shuffle=c.shuffle)

        self.train = train.reset_index(drop=True)
        self.validate = validate.reset_index(drop=True)
        self.hold = hold.reset_index(drop=True);

        return self

    class Config:
        def __init__(
            self
        ):
            self.train = 0;
            self.validate = 0;
            self.seed = None;
            self.shuffle = False;

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
