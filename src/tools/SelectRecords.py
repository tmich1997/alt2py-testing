import pandas as pd
import re

class SelectRecords:
    def __init__(self,xml=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);

    def parse_range_expressions(self,text,df_name="new_df"):
        c = self.config;
        out = ""
        pattern = re.compile("[^\d\+\s-]")
        match = pattern.match(text);
        if match:
            raise Exception("Range Expression Can't Contain Words!")
        if "-" in text:
            pattern = re.compile("(\d*)\s*-\s*(\d*)")
            match = pattern.match(text);
            m1 = match.group(1)
            m2 = match.group(2)

            if m1:
                out+=f"({df_name}.index + {c.index} >= {m1})"
            if m2:
                if m1:
                    out += " & "
                out+=f"({df_name}.index + {c.index} <= {m2})"
            return f"({out})"

        elif "+" in text:
            pattern = re.compile("(\d*)\+")
            match = pattern.match(text);
            m1 = match.group(1)
            out = f"{df_name}.index + {c.index} >= {m1}"
            return f"({out})"
        else:
            pattern = re.compile("(\d*)")
            match = pattern.match(text);
            m1 = match.group(1)
            out = f"{df_name}.index + {c.index} == {m1}"
            return f"({out})"

    def load_xml(self,xml):
        c = self.config;
        c.index = 1
        values = xml.find(".//Configuration//Value").text.split("\n")
        print(values)
        for v in values:
            c.conditions.append(self.parse_range_expressions(v))

    def execute(self,input_datasource):
        c = self.config;

        new_df = input_datasource.copy();

        print(c.conditions)

        joined_conditions = " | ".join(c.conditions)
        new_df = eval(f"new_df[{joined_conditions}]")
        return new_df.reset_index(drop=True)

    class Config:
        def __init__(
            self
        ):
            self.conditions=[];
            self.index = 0;


        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
