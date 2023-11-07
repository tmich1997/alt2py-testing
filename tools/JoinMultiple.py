import pandas as pd;
from tools.Select import Select
import re

class JoinMultiple:
    def __init__(self,xml=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        # elif xml:
        #     self.load_xml(xml) NEED TO LOAD XML IN EXECUTE.
        elif json:
            self.load_json(json);

        self.unique = None;
        self.duplicates = None;
        self.xml = xml;

    def load_xml(self,xml):
        c = self.config;

        c.by_position = xml.find(".//Properties//Configuration//JoinByRecPos").get("value")=="True"
        c.inner = xml.find(".//Properties//Configuration//OutputJoinOnly").get("value")=="True"

        join_infos = xml.find(".//Configuration//JoinFields")
        c.fields = []
        if not c.by_position:
            c.names = [j.get("connection") for j in join_infos]
            for join_info in join_infos:
                prefix = ''
                if re.match(rf'#\d$',join_info.get("connection")):
                    prefix = f'Input_{join_info.get("connection")}_'
                else:
                    prefix = f'{join_info.get("connection")}_'
                c.fields.append([f'{prefix}{f.get("field")}' for f in join_info])


    def join_by_pos(self,dfs):
        c = self.config;

        merged_dfs = pd.concat(dfs, axis=1)

        if c.inner:
            length = min([len(df) for df in dfs])
            merged_dfs = merged_dfs.head(length)

        return merged_dfs

    def join_by_key(self,dfs):
        c = self.config;
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            merged_dfs = dfs.pop(0);

            for i, next_df in enumerate(dfs):
                merged_dfs = pd.merge(
                    merged_dfs,
                    next_df,
                    left_on=c.fields[i],
                    right_on=c.fields[i+1],
                    how="inner" if c.inner else "outer",
                    sort=True
                )
        return merged_dfs

    def execute(self,input_datasources):
        c = self.config;

        dfs = None;
        if self.xml:
            c.names = [df["name"] for df in input_datasources]
            self.load_xml(self.xml)
            dfs = {df["name"]:df["data"].copy() for df in input_datasources}

            dfs = [dfs[n] for n in c.names]
            #SELECT TOOL CONFIG IS PREFACED WITH NAME
            for i,df in enumerate(dfs):
                prefix = f'Input_{c.names[i]}_' if re.match('^#\d$',c.names[i]) else f'{c.names[i]}_'
                df.columns = [f"{prefix}{col}" for col in df.columns]

        else:
            dfs = [df.copy() for df in input_datasources]

        new_df = None;
        if c.by_position:
            new_df = self.join_by_pos(dfs)
        else:
            new_df = self.join_by_key(dfs)

        if self.xml:
            new_df = Select(xml = self.xml.find(".//SelectConfiguration")).execute(new_df)

            rename_back = {} # IF THE COLUMN WASN't RENAMED AND DOESN'T NEED TO BE CHANGE IT BACK

            actual_renames = []

            for f in self.xml.find(".//SelectConfiguration//Configuration//SelectFields"):
                if f.get("rename") is not None:
                    actual_renames.append(f.get("rename"))

            for col in new_df.columns:
                if col in actual_renames:
                    continue
                else:
                    prefixes = [f'Input_{n}_' if re.match('^#\d$',n) else f'{n}_' for n in c.names]
                    prefixes_or = '|'.join(prefixes)
                    pattern = f'({prefixes_or})(.*)'
                    match = re.match(pattern,col)
                    if match:
                        if match.group(2) not in rename_back.values():
                            rename_back[col] = match.group(2)
            new_df = new_df.rename(columns = rename_back)

  # <SelectFields>
  #   <SelectField field="First_Name" selected="True" rename="First_Name" />
  #   <SelectField field="Third_Name" selected="True" rename="Third_Name" />
  #   <SelectField field="*Unknown" selected="True" />
  # </SelectFields>
        return new_df

    class Config:
        def __init__(
            self
        ):
            self.fields=[];
            self.names=[]; # NAMES ORDER COMES FROM JOININFO FIELDS
            self.by_position = False;
            self.inner = False;

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
