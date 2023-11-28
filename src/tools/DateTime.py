import pandas as pd
from datetime import datetime
import re

class DateTime:
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


    def load_json(self,kwargs):
        c = self.config;

    def load_xml(self,xml):
        c = self.config;

        c.field = xml.find(".//Configuration//InputFieldName").text
        c.to_string = xml.find(".//Configuration//IsFrom").get("value") == "True"
        c.pattern = xml.find(".//Configuration//Format").text
        c.label = xml.find(".//Configuration//OutputFieldName").text

    def convert_pattern(self):
        c = self.config;

        lp = "(^|[\, \-\/\:])"
        rp = "($|[\, \-\/\:])"
        c.pattern = re.sub(lp+"(d)"+rp, r"\1%-d\3", c.pattern)
        c.pattern = re.sub(lp+"(day)"+rp, r"\1%A\3", c.pattern)
        c.pattern = re.sub(lp+"(dd)"+rp, r"\1%d\3", c.pattern)
        c.pattern = re.sub(lp+"(dy)"+rp, r"\1%a\3", c.pattern)
        c.pattern = re.sub(lp+"(EEEE)"+rp, r"\1%A\3", c.pattern)
        c.pattern = re.sub(lp+"(M)"+rp, r"\1%-m\3", c.pattern)
        c.pattern = re.sub(lp+"(MM)"+rp, r"\1%m\3", c.pattern)
        c.pattern = re.sub(lp+"(MMM)"+rp, r"\1%b\3", c.pattern)
        c.pattern = re.sub(lp+"(MMMM)"+rp, r"\1%B\3", c.pattern)
        c.pattern = re.sub(lp+"(Mon)"+rp, r"\1%b\3", c.pattern)
        c.pattern = re.sub(lp+"(Month)"+rp, r"\1%B\3", c.pattern)
        c.pattern = re.sub(lp+"(yy)"+rp, r"\1%y\3", c.pattern)
        c.pattern = re.sub(lp+"(yyyy)"+rp, r"\1%Y\3", c.pattern)

        c.pattern = re.sub(lp+"(ahh)"+rp, r"\1%p\3", c.pattern)
        c.pattern = re.sub(lp+"(H)"+rp, r"\1%-H\3", c.pattern)
        c.pattern = re.sub(lp+"(HH)"+rp, r"\1%H\3", c.pattern)
        c.pattern = re.sub(lp+"(hh)"+rp, r"\1%H\3", c.pattern)
        c.pattern = re.sub(lp+"(mm)"+rp, r"\1%M\3", c.pattern)
        c.pattern = re.sub(lp+"(ss)"+rp, r"\1%S\3", c.pattern)


    def execute(self,input_datasource):
        c = self.config;
        new_df = input_datasource.copy();
        self.convert_pattern()

        if not c.to_string:
            def strpt(d):
                return datetime.strptime(d,c.pattern) if not pd.isnull(d) else d

            new_df[c.label] = new_df[c.field].apply(strpt).astype('datetime64[ns]')

        else:
            def strft(d):
                return d.strftime(c.pattern) if not pd.isnull(d) else d

            new_df[c.label] = new_df[c.field].apply(strft).astype(pd.StringDtype())

        return new_df.reset_index(drop=True)

    class Config:
        def __init__(
            self
        ):
            self.to_string = False
            self.field = None
            self.pattern = None
            self.label = None

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
