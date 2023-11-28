import pandas as pd
import re
from functools import reduce;

class TextToColumns:
    def __init__(self,yxdb_tool=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        elif json:
            self.load_json(json);

    def load_yxdb_tool(self,tool, execute=True):

        c = self.config;
        xml = tool.xml;

        config = xml.find("Properties").find("Configuration")

        c.field = config.find("Field").text
        c.num_fields = int(config.find("NumFields").get('value'))
        delim = config.find("Delimeters").get('value')
        c.delim = delim.replace("\\n", "\n").replace("\\t", "\t").replace("\s", " ")
        flagBin = self.flagValToBin(int(config.find("Flags").get('value')))

        c.ign_double_quote = flagBin[7]
        c.ign_parenth = flagBin[6]
        c.ign_single_quote = flagBin[4]
        c.skip_empty = flagBin[3]
        c.ign_brackets = flagBin[2]

        if c.num_fields > 1:
            c.error_handle = config.find("ErrorHandling").text
            _RootName = config.find("RootName").text
            if _RootName is not None:
                c.root_name = re.sub(r'\s+|\n', '', _RootName)

        if execute:
            df = tool.get_input("Input")
            next_df = self.execute(df)
            tool.data["Output"] = next_df

    def applier(self,text):
        cf = self.config;
        delim = cf.delim
        ign_brackets = cf.ign_brackets
        ign_parenth = cf.ign_parenth
        ign_doubleq = cf.ign_double_quote
        ign_singleq = cf.ign_single_quote
        skip_empty = cf.skip_empty

        regex = '[' + delim + ']'
        ignorers = [];

        if ign_brackets:
            ignorers.append([0,['[',']']])
        if ign_parenth:
            ignorers.append([0,['(',')']])
        if ign_doubleq:
            ignorers.append([0,['"','"']])
        if ign_doubleq:
            ignorers.append([0,["'","'"]])

        arr = [];

        current_str = '';
        delim_set = set(delim)

        delim_lookup = {};
        for d in delim:
            delim_lookup[d] = True

        for char in text:
            for ig in ignorers:
                if ig[1][0] == ig[1][1] and char==ig[1][0]:
                    ig[0]=(ig[0]+1)%2;
                elif ig[1][0]==char:
                    ig[0]+=1;
                elif ig[1][1]==char:
                    ig[0]-=1

            if not reduce(lambda acc, arr: acc and (len(arr) > 0 and arr[0] == 0), ignorers, True): #True if char is enclosed
                current_str += char
            elif delim_lookup.get(char):
                if not skip_empty or current_str:
                    arr.append(current_str)
                    current_str=''
            else:
                current_str += char

        if len(current_str)>0:
            arr.append(current_str)
        return pd.Series(arr)

    def build_regex(self):
        c = self.config
        delim = c.delim
        ign_brackets = c.ign_brackets
        ign_parenth = c.ign_parenth
        ign_doubleq = c.ign_double_quote
        ign_singleq = c.ign_single_quote
        skip_empty = c.skip_empty

        regex = '[' + delim.replace('[','\[').replace(']','\]').replace('(','\(').replace(')','\)') + ']'
        if skip_empty:
            regex += '+'
        if ign_brackets:
            regex += '(?![^\[]*\])'
        if ign_parenth:
            regex += '(?![^\(]*\))'

        return regex

    def flagValToBin(self,val):
        binary_string = bin(val)[2:]  # Remove the '0b' prefix from the binary string
        binary_array = [int(bit) for bit in binary_string]

        while len(binary_array) < 8:
            binary_array.insert(0, 0)

        return binary_array

    def execute(self,input_datasource):
        df = input_datasource.copy()
        c = self.config
        field = c.field;
        delim = c.delim;
        num_fields = c.num_fields;
        ign_brackets = c.ign_brackets;
        ign_parenth = c.ign_parenth;
        ign_doubleq = c.ign_double_quote;
        ign_singleq = c.ign_single_quote;
        skip_empty = c.skip_empty;
        root_name = c.root_name;

        if ign_doubleq or ign_singleq:
            df_split = df[field].apply(self.applier)
        else:
            pattern = self.build_regex()
            # Split the 'text_column' based on the pattern and create a new DataFrame
            df_split = df[field].str.split(pattern, expand=True)

        # Rename the columns with the original column name followed by a number
        df_split.columns = [f'{root_name}{i+1}' for i in range(df_split.shape[1])]

        num_existing_columns = df_split.shape[1]
        num_columns_to_add = num_fields - num_existing_columns


        if num_columns_to_add > 0:
            df_extend_nulls = pd.DataFrame()
            # Create a list of column names for the new columns
            new_column_names = [f'{root_name}{i+1}' for i in range(num_existing_columns, num_fields)]

            for column_name in new_column_names:
                df_extend_nulls[column_name] = None

            df_split = pd.concat([df_split,df_extend_nulls], axis=1)

        df_out = pd.concat([df, df_split], axis=1)

        if num_fields <=1:
            columns = df.columns.tolist() + ['order_index'];
            # Create a new DataFrame with the order_index column
            df_out = df_out.reset_index().rename(columns={'index': 'order_index'})
            df_out = df_out.melt(id_vars=columns)
            df_out['variable'] = df_out['variable'].astype(int)
            df_out = df_out.sort_values(by=['order_index', 'variable'], ascending=[True, True])
            df_out = df_out.drop(columns=[field,"variable",'order_index'])
            df_out.dropna(subset=['value'], inplace=True)
            df_out.rename(columns={'value': field}, inplace=True)
            df_out.reset_index(drop=True, inplace=True)
        return(df_out)

    class Config:
        def __init__(
            self,
            field=None,
            root_name='',
            num_fields=3,
            delim=',',
            error_handle=None,
            ign_brackets=False,
            ign_parenth=False,
            ign_single_quote=False,
            ign_double_quote=False,
            skip_empty=False
        ):
            self.field=field
            self.root_name=root_name
            self.num_fields=num_fields
            self.delim=delim
            self.error_handle=error_handle
            self.ign_brackets=ign_brackets
            self.ign_parenth=ign_parenth
            self.ign_single_quote=ign_single_quote
            self.ign_double_quote=ign_double_quote
            self.skip_empty=skip_empty

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
