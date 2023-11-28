from .Config import Config;
import pandas as pd;
import numpy as np;
import re;

class Clean:
    def __init__(self,xml=None,json=None,config=None):
        # LOAD DEFAULTS
        self.config = Config(
            fields = None,
            filter_na_cols = False,
            filter_na_rows = False,
            replace_na_blank = False,
            replace_na_zero = False,
            trim_whitespace = False,
            remove_dup_space = False,
            remove_all_space = False,
            remove_letters = False,
            remove_numbers = False,
            remove_punctuation = False,
            modify = False,
            modifier = "title"
        );
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);

    def load_xml(self,xml):
        c = self.config;

        values = {int(re.sub(r"[\(\)]",'', v.get("name").split(" ")[-1])):v.text for v in xml.find(".//Configuration")}

        c.fields = re.sub('^\"|\"$',"",values[11]).split('","')
        c.filter_na_cols = values[135]=="True"
        c.filter_na_rows = values[136]=="True"
        c.replace_na_blank = values[84]=="True"
        c.replace_na_zero = values[117]=="True"
        c.trim_whitespace = values[15]=="True"
        c.remove_dup_space = values[109]=="True"
        c.remove_all_space = values[122]=="True"
        c.remove_letters = values[53]=="True"
        c.remove_numbers = values[58]=="True"
        c.remove_punctuation = values[70]=="True"
        c.modify = values[77]=="True"
        c.modifier = values[81]

    def execute(self,input_datasource):
        c = self.config;

        new_df = input_datasource.copy()

        if c.fields is None:
            c.fields = input_datasource.columns.tolist();

        if c.filter_na_cols:#APPLIES TO ALL COLUMNS
            new_df = new_df.dropna(axis=1, how='all')
            c.fields = [item for item in c.fields if item in new_df.columns]

        if c.filter_na_rows:
            new_df = new_df.dropna(axis=0, how='all')

        string_columns = new_df[c.fields].select_dtypes(include=[pd.StringDtype()]).columns.tolist()
        numeric_columns = new_df[c.fields].select_dtypes(include=np.number).columns.tolist()

        if c.replace_na_blank:
            new_df[string_columns] = new_df[string_columns].replace({pd.NA: ''})

        if c.replace_na_zero:
            new_df[numeric_columns] = new_df[numeric_columns].replace({pd.NA: 0})

        if c.remove_letters:
            new_df[string_columns] = new_df[string_columns].apply(lambda x: x.str.replace(r'[a-zA-Z]+', '',regex=True))

        if c.remove_numbers:
            new_df[string_columns] = new_df[string_columns].apply(lambda x: x.str.replace(r'[0-9]+', '',regex=True))

        if c.remove_punctuation:
            new_df[string_columns] = new_df[string_columns].apply(lambda x: x.str.replace(r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', '',regex=True))

        if c.trim_whitespace:
            new_df[string_columns] = new_df[string_columns].apply(lambda x: x.str.strip())

        if c.remove_dup_space:
            new_df[string_columns] = new_df[string_columns].apply(lambda x: x.str.replace(r'\s+', ' ',regex=True))

        if c.remove_all_space:
            new_df[string_columns] = new_df[string_columns].apply(lambda x: x.str.replace(r'\s+', '',regex=True))

        if c.modify:
            if c.modifier=="title":
                new_df[string_columns] = new_df[string_columns].apply(lambda x: x.str.title())
            elif c.modifier=="upper":
                new_df[string_columns] = new_df[string_columns].apply(lambda x: x.str.upper())
            elif c.modifier=="lower":
                new_df[string_columns] = new_df[string_columns].apply(lambda x: x.str.lower())
            else:
                raise Exception("Unknown modifier")

        return new_df
