import pandas as pd
import re
from functools import reduce,partial;
from collections import OrderedDict;
from shapely.ops import unary_union;
from _utils import Aggregators


class Summarise:
    def __init__(self,yxdb_tool=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        elif json:
            self.load_json(json);

    def add_aggregator(self,field,rename,aggregator,**kwargs):
        c= self.config
        if field in c.aggregators:
            c.aggregators[field].append(partial(aggregator,**kwargs))
        else:
            c.aggregators[field] = [partial(aggregator,**kwargs)]
        c.agg_renames.append(rename)
        c.order.append(rename)

    def add_grouping(self,field,rename):
        c= self.config
        c.group_names.append(field)
        c.group_renames.append(rename)
        c.order.append(rename)

    def map_xml_to_kwargs(self,fields):
        arg_map = {
            "Concat_Start":"start",
            "Separator":"sep",
            "Concat_End":"end"
        }

        args = {}

        for f in fields:
            args[arg_map[f.tag]] = f.text
        return args

    def load_yxdb_tool(self,tool, execute=True):
        c = self.config
        xml = tool.xml
        summary_fields = xml.find("Properties/Configuration/SummarizeFields");
        for field in summary_fields:
            field_name = field.get('field')
            action = field.get('action')
            rename = field.get('rename')
            if action=="GroupBy":
                self.add_grouping(field_name,rename)
            else:
                other_args = self.map_xml_to_kwargs(field)
                self.add_aggregator(field_name,rename,Aggregators.get_by_name(action),**other_args)
        if execute:
            df = tool.get_input("Input")
            next_df = self.execute(df)
            tool.data["Output"] = next_df

    def execute(self,input_datasource):
        c= self.config
        df = input_datasource.copy()
        if len(c.group_names)>0:
            grouped = df.groupby(c.group_names)
            if len(c.aggregators)==0:
                result_df = pd.DataFrame(list(grouped.groups.keys()))
            else:
                result_df = grouped.agg(c.aggregators).reset_index()
        else:
            if len(c.aggregators)==0:
                result_df = df
            else:
                result_df = df.agg(c.aggregators).reset_index(drop=True).T.stack().to_frame().T

        result_df.columns = c.group_renames + c.agg_renames
        result_df.reset_index(drop=True,inplace=True)

        result_df = result_df.loc[:,c.order]



        return result_df

    class Config:
        def __init__(
            self
        ):
            self.aggregators = OrderedDict();
            self.group_names = [];
            self.group_renames = [];
            self.agg_renames = []; #agg_names
            self.order = []

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
