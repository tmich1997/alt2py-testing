import pandas as pd
from sklearn.model_selection import train_test_split

class Sample:

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

        c.train = json["train"]
        c.seed = json["seed"] if "seed" in json else None;

    def load_yxdb_tool(self,tool,execute=True):
        c = self.config;
        xml = tool.xml;

        values = {v.get("name"):int(v.text) for v in xml.find(".//Configuration")}

        c.train = values["estimation pct"]/100
        c.validate = values["validation pct"]/100 #(100 - values["estimation pct"])
        c.seed = values["rand seed"]
        c.shuffle = False;

        if execute:
            df = tool.get_input("Input")
            out = self.execute(df)

            tool.data["Estimation"] = out.train
            tool.data["Validation"] = out.validate
            tool.data["Holdout"] = out.hold

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
            self.train = .75;
            self.validate = .25;
            self.seed = None;
            self.shuffle = True;

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
