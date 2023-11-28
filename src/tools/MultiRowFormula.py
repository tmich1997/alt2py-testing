import pandas as pd;
import numpy as np;
import re
from tools.Formula import Functions
from tools.Select import dtype_map


class MultiRowFormula:
    def __init__(self,xml=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);

    def load_xml(self,xml):
        # <Configuration>
        # <UpdateField value="True" />
        # <UpdateField_Name>Year</UpdateField_Name>
        # <CreateField_Name>NewField</CreateField_Name>
        # <CreateField_Type>Int32</CreateField_Type>
        # <CreateField_Size>254</CreateField_Size>
        # <OtherRows>Empty</OtherRows>
        # <NumRows value="1" />
        # <Expression>IF IsNull([Year])
        # THEN [Row-1:Year]
        # ELSE [Year]
        # ENDIF</Expression>
        # <GroupByFields />

        c = self.config;

        c.expression =  xml.find(".//Configuration/Expression").text
        c.num_rows = int(xml.find(".//Configuration/NumRows").get("value"))
        c.unknown = xml.find(".//Configuration/OtherRows").text


        if xml.find(".//Configuration/UpdateField").get("value")=="True":
            c.field = xml.find(".//Configuration/UpdateField_Name").text
        else:
            c.field = xml.find(".//Configuration/CreateField_Name").text
            c.type = dtype_map[xml.find(".//Configuration/CreateField_Type").text]
            c.size = xml.find(".//Configuration/CreateField_Size").text

        for f in xml.find(".//Configuration/GroupByFields"):
            c.groupings.append(f.get('field'))

    def format_multirow_formula(self,index,column_names):
        pattern = re.compile(rf'series\[\'Row([\+\-]\d+):(.*?)\'\]', re.IGNORECASE)
        sub = rf"new_df['\2'].at[eval('{index}\1')]"
        text = Functions.parse_formula(self.config.expression,df_name="series",column_names=column_names)
        return re.sub(pattern,sub,text)

    def apply_formula(self,df):
        c = self.config;
        null_row = []
        null_row2 = []
        if c.unknown=="NULL":
            null_row=[pd.NA]*len(df.columns)
            null_row2 = null_row
        elif c.unknown=="Empty":
            for col in df.columns:
                if pd.api.types.is_bool_dtype(df[col]):
                    null_row.append(pd.NA)
                elif pd.api.types.is_numeric_dtype(df[col]):
                    null_row.append(0)
                elif pd.api.types.is_string_dtype(df[col]):
                    null_row.append('')
                else:
                    null_row.append(pd.NA)
            null_row2 = null_row
        else:
            null_row = df.iloc[0].tolist()
            null_row2 = df.iloc[len(df)-1].tolist()


        null_df_start = pd.DataFrame([null_row]*c.num_rows,columns=df.columns,index=[-i for i in range(1,c.num_rows+1)])
        null_df_end = pd.DataFrame([null_row2]*c.num_rows,columns=df.columns,index=[i for i in range(len(df),c.num_rows+len(df))])
        new_df = pd.concat([null_df_start,df,null_df_end]).astype(df.dtypes)

        for i,series in new_df.loc[0:len(df)-1].iterrows():
            exp = self.format_multirow_formula(i,new_df.columns)
            new_element = eval(exp)
            if pd.api.types.is_bool_dtype(df[c.field]):
                new_df[c.field].at[i] = not not new_element
            else:
                new_df[c.field].at[i] = new_element
            # new_df["Year"] = eval(x)

        return new_df.loc[0:len(df)-1]

    def execute(self,input_datasource):
        c = self.config;
        new_df = input_datasource.copy()
        if c.field not in new_df:
            new_df[c.field] = pd.NA
            new_df[c.field] = new_df[c.field].astype(c.type)

        if len(c.groupings):
            dfs_to_concat = []
            for i,group in new_df.groupby(c.groupings):
                dfs_to_concat.append(self.apply_formula(group.reset_index(drop=True)))

            new_df = pd.concat(dfs_to_concat).reset_index(drop=True)
        else:
            new_df = self.apply_formula(new_df)

        if c.type:
            new_df[c.field] = new_df[c.field].astype(c.type)
            if "." in c.size:
                new_df[c.field] = new_df[c.field].apply(lambda x: Functions.Round(x,10**(-int(c.size.split(".")[-1]))))
        return new_df;

    class Config:
        def __init__(
            self
        ):
            self.num_rows = 1;
            self.field = None;
            self.groupings = [];
            self.expression = None;
            self.type = None;
            self.size = None;
            self.unknown = pd.NA;

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
