import pandas as pd
import re
from functools import reduce;
from .Formula import Functions
from .Select import dtype_map

class GenerateRows:
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

        updateField = xml.find(".//Configuration//UpdateField").get('value')=="True"

        if updateField:
            c.mode = "UPDATE"
            c.field = xml.find(".//Configuration//UpdateField_Name").text
        else:
            c.mode = "NEW"
            c.field = xml.find(".//Configuration//CreateField_Name").text
            c.field_type = dtype_map[xml.find(".//Configuration//CreateField_Type").text]

        c.initialiser = xml.find(".//Configuration//Expression_Init").text
        c.should_loop = xml.find(".//Configuration//Expression_Cond").text
        c.on_loop = xml.find(".//Configuration//Expression_Loop").text

        if execute:
            if len(tool.inputs)>0:
                df = tool.get_input("Input")
                next_df = self.execute(df)
            else:
                next_df = self.execute()

            tool.data["Output"] = next_df

    def applier(self,series):
        c = self.config;
        c_row = eval(c.initialiser)
        series[c.field] = c_row
        con = eval(c.should_loop)
        rows = {c.field:[]}
        while(con):
            rows[c.field].append(c_row)
            c_row = eval(c.on_loop)
            series[c.field] = c_row
            con = eval(c.should_loop)
        new_df = pd.DataFrame(rows)
        result_df = pd.DataFrame.from_records([series]*len(rows[c.field]))
        if c.field_type:
            result_df[c.field] = new_df[c.field].astype(c.field_type)
        else:
            result_df[c.field] = new_df[c.field]
        return result_df

    def execute(self,input_datasource=None):
        c = self.config
        if input_datasource is not None:

            df = input_datasource.copy()

            c.initialiser = Functions.parse_formula(c.initialiser,column_names=[c.field]+df.columns.tolist(),df_name="series")
            c.should_loop = Functions.parse_formula(c.should_loop,column_names=[c.field]+df.columns.tolist(),df_name="series")
            c.on_loop = Functions.parse_formula(c.on_loop,column_names=[c.field]+df.columns.tolist(),df_name="series")

            df_list = df.apply(
                self.applier,
                axis=1
            )

            df_list = [df for df in df_list if not df.empty] #prevents unwanted unit conversions
            new_df = pd.concat(df_list, ignore_index=True)

        else:
            initialiser = Functions.parse_formula(c.initialiser,column_names=[c.field],df_name="series")
            should_loop = Functions.parse_formula(c.should_loop,column_names=[c.field],df_name="series")
            on_loop = Functions.parse_formula(c.on_loop,column_names=[c.field],df_name="series")

            series = {c.field:eval(initialiser)}

            con = eval(should_loop)
            rows = []
            while(con):
                rows.append(series)
                series = {c.field:eval(on_loop)}
                con = eval(should_loop)
                # runs 1 too many times
            df = pd.DataFrame(rows,dtype=c.field_type)
            new_df = df

        return new_df

    class Config:
        def __init__(
            self,
            field = None,
            mode = "NEW", #NEW OR UPDATE
            field_type = None,
            initialiser = None,
            on_loop = None,
            condition = None
        ):
            self.field=field
            self.mode=mode
            self.field_type=field_type
            self.initialiser=initialiser
            self.on_loop=on_loop
            self.condition=condition

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
