import pandas as pd
import re
from functools import reduce,partial;
from collections import OrderedDict;
from shapely.ops import unary_union;

class Aggregators:

    @staticmethod
    def get_by_name(name):
        names = {
            'Sum':Aggregators.sum,
            'Min':Aggregators.min,
            'Max':Aggregators.max,
            'Concat':Aggregators.concat,
            'Count':Aggregators.count,
            'First':Aggregators.first,
            'Last':Aggregators.last,
            'Longest':Aggregators.longest,
            'Shortest':Aggregators.shortest,
            'Avg':Aggregators.avg,
            'Median':Aggregators.median,
            'Mode':Aggregators.mode,
            'StdDev':Aggregators.std_dev,
            'Variance':Aggregators.var,
            'SpatialObjCombine':Aggregators.spatial_combine,
            'SpatialObjConvexHull':Aggregators.convex_hull,
            'CountBlank':Aggregators.count_blanks,
            'CountNonBlank':Aggregators.count_non_blanks
        }
        if name not in names:
            return;
        return names[name]
    @staticmethod
    def sum(x):
        return sum(x)

    @staticmethod
    def min(x):
        return x.min()

    @staticmethod
    def max(x):
        return x.max()

    @staticmethod
    def concat(x,**kwargs):
        start = kwargs["start"] if "start" in kwargs else "";
        sep = kwargs["sep"] if "sep" in kwargs else ",";
        end = kwargs["end"] if "end" in kwargs else "";
        return start + x.str.cat(sep=sep) + end

    @staticmethod
    def count(x):
        return len(x)

    @staticmethod
    def first(x):
        return x.iloc[0]

    @staticmethod
    def last(x):
        return x.iloc[-1]

    @staticmethod
    def longest(x):
        string_lengths = x.str.len()
        max_length = string_lengths.max()
        longest_strings = x[string_lengths == max_length]
        return longest_strings.iloc[0]

    @staticmethod
    def shortest(x):
        string_lengths = x.str.len()
        min_length = string_lengths.min()
        longest_strings = x[string_lengths == min_length]
        return longest_strings.iloc[0]

    @staticmethod
    def avg(x):
        return x.mean()

    @staticmethod
    def median(x):
        return x.median()

    @staticmethod
    def mode(x):
        return x.mode().iloc[0]

    @staticmethod
    def std_dev(x):
        return x.std()

    @staticmethod
    def var(x):
        return x.var()

    @staticmethod
    def spatial_combine(x):
        return unary_union(x)

    @staticmethod
    def convex_hull(x):
        return unary_union(x).convex_hull

    @staticmethod
    def count_blanks(x,xml=None):
        filtered_series = x.loc[lambda x: x.isna() | (x == '')]
        return len(filtered_series)

    @staticmethod
    def count_non_blanks(x,xml=None):
        filtered_series = x.dropna().loc[lambda a: a != '']
        return len(filtered_series)

    @staticmethod
    def count_non_null(x,xml=None):
        filtered_series = x.dropna()
        return len(filtered_series)



class Summarise:
    def __init__(self,xml=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
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

    def load_xml(self,xml):
        c = self.config

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
