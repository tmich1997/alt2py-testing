import pandas as pd
import re
from functools import reduce;

class RegEx:
    def __init__(self,yxdb_tool=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        elif json:
            self.load_json(json);

    def load_yxdb_tool(self,tool,execute=True):
        c = self.config
        xml = tool.xml
        config = xml.find('Properties/Configuration')

        c.field = config.find("Field").text
        c.pattern = config.find("RegExExpression").get("value")
        c.case_insensitve = config.find("CaseInsensitve").get("value")=="True"
        c.method = config.find("Method").text

        if c.method=="Replace":
            c.method="replace"
            replace_config = config.find("Replace")
            c.replace_pattern = replace_config.get("expression")
            c.copy_unmatched = replace_config.find("CopyUnmatched").get("value")=="True"
        elif c.method=="ParseSimple":
            c.method="parse"
            parse_config = config.find("ParseSimple")
            c.to_rows = parse_config.find("SplitToRows").get("value")=="True"
            if not c.to_rows:
                c.root_name = parse_config.find("RootName").text;
                c.num_fields =  int(parse_config.find("NumFields").get("value"))
                c.on_error = parse_config.find("ErrorHandling").text #Warn Ignore Error
        elif c.method=="ParseComplex":
            c.method="tokenize"
            parse_config = config.find("ParseComplex")
            c.new_fields = [[f.get("field"),f.get("type"),f.get("size")] for f in parse_config.findall("Field")]
        elif c.method=="Match":
            c.method="match"
            match_config = config.find("Match")
            c.new_fields = [match_config.find("Field").text]

        if execute:
            df = tool.get_input("Input")
            next_df = self.execute(df)
            tool.data["Output"] = next_df

    def regex_tokenize(self,text):
        c = self.config
        flags = re.IGNORECASE if c.case_insensitive else 0;

        matches = re.search(c.pattern, text,flags=flags)
        out = []

        for i,f in enumerate(c.new_fields):
            if matches:
                out.append(matches.group(i+1))
            else:
                out.append(None)
        return out

    def regex_replace(self,text):
        c = self.config

        flags = re.IGNORECASE if c.case_insensitive else 0;
        compiled_pattern = re.compile(c.pattern,flags=flags)
        match = compiled_pattern.search(text)

        if match:
            # Replace the matched text using the replacement string and dollar signs
            replaced_text = compiled_pattern.sub(c.replace_pattern.replace("$","\\"), text)
            return replaced_text
        else:
            # Return the input string as-is if no matches found
            return text if c.copy_unmatched else "";

    def regex_to_columns(self,text):
        c = self.config

        flags = re.IGNORECASE if c.case_insensitive else 0;
        out = []
        match = re.search(c.pattern, text,flags=flags)
        ##c.num_fields = 2
        while match and (len(out)<c.num_fields or c.num_fields is None):
            out.append(match.group(0))
            text = text[match.end():]
            match = re.search(c.pattern, text,flags=flags)

        if c.num_fields is not None and match:
            out.append(text[match.start():])
        return out

    def execute(self,input_datasource):
        new_df = input_datasource.copy();
        c = self.config;
        print(c)
        if c.method=="replace":
            new_df[c.field] = new_df[c.field].apply(self.regex_replace)

        elif c.method=="parse":
            new_cols = new_df[c.field].apply(self.regex_to_columns)
            new_cols = pd.DataFrame(new_cols.tolist())
            if c.root_name is not None:
                new_cols.columns = [c.root_name+str(col+1) for col in new_cols.columns]
            new_df = pd.concat([new_df,new_cols], axis=1)

            if c.to_rows:
                new_df = new_df.reset_index().rename(columns={'index': 'order_index'})
                new_df = new_df.melt(id_vars=input_datasource.columns.tolist()+['order_index'])
                new_df['variable'] = new_df['variable'].astype(int)
                new_df.sort_values(by=['order_index', 'variable'], ascending=[True, True],inplace=True)
                new_df.drop([c.field,'variable','order_index'], axis=1, inplace=True)
                new_df.rename(columns={'value':c.field},inplace=True)
                new_df.reset_index(drop=True,inplace=True)
                new_df = new_df[new_df[c.field].notna()]

        elif c.method=="tokenize":
            new_cols = new_df[c.field].apply(self.regex_tokenize)
            new_cols = pd.DataFrame(new_cols.tolist())
            new_cols.columns = [f[0] for f in c.new_fields]
            new_df = pd.concat([new_df,new_cols], axis=1)

        elif c.method=="match":
            new_df = new_df.assign(**{c.new_fields[0]: new_df[c.field].str.match(c.pattern)})

        return new_df

    class Config:
        def __init__(
            self
        ):
            self.field = None
            self.pattern = None
            self.case_insensitive = True
            self.method = None

            self.replace_pattern = None
            self.copy_unmatched = None
            self.to_rows = None

            self.root_name = None
            self.num_fields = 2
            self.on_error = None
            self.new_fields = None

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
