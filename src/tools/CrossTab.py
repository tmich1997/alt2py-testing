import pandas as pd;
from functools import partial
from tools.Summarise import Aggregators as agg;
from tools.Sort import Sort;


class CrossTab:
    def __init__(self,xml=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);

        self.unique = None;
        self.duplicates = None;

    def load_xml(self,xml):
        c = self.config;

        sep = xml.find(".//Configuration//Methods//Separator")

        if sep is not None:
            sep = sep.text.replace("\s"," ")
        method_map = {
            "Sum":agg.sum,
            "Avg":agg.avg,
            "Count":agg.count_non_null,
            "CountWithNulls":agg.count,
            "First":agg.first,
            "Last":agg.last,
            "Concat":partial(agg.concat,sep=sep)
        }

        c.groupings = [f.get("field") for f in xml.find(".//Configuration//GroupFields")]
        c.header = xml.find(".//Configuration//HeaderField").get("field")
        c.value_field = xml.find(".//Configuration//DataField").get("field")
        c.method = method_map[xml.find(".//Configuration//Methods//Method").get("method")]

    def execute(self,input_datasource):
        c = self.config;
        new_df = input_datasource.copy()

        for header in c.header:
            new_df[c.header] = new_df[c.header].astype(pd.StringDtype())
            new_df[c.header] = new_df[c.header].str.replace(" ","_")
            new_df[c.header] = new_df[c.header].fillna('_Null_')

        indices = new_df[c.groupings]
        filled_indices = indices.astype("string").fillna("___NA___")

        # Create a crosstab
        crosstab_df = pd.crosstab(
            index=[filled_indices[col] for col in filled_indices.columns],
            columns=new_df[c.header],
            values=new_df[c.value_field],
            aggfunc=c.method
        )

        # Reset the index to get the columns 'presidentNumber', 'President', and 'Vice President'
        crosstab_df = crosstab_df.reset_index().rename_axis(None, axis=1)
        crosstab_df.columns = crosstab_df.columns.astype("object")

        crosstab_df[c.groupings] = crosstab_df[c.groupings].replace("___NA___",pd.NA).astype(indices.dtypes)

        crosstab_df = Sort(fields = c.groupings).execute(crosstab_df)
        return crosstab_df

    class Config:
        def __init__(
            self
        ):
            self.groupings = []
            self.header = None;
            self.value_field = None
            self.method = "first"
            self.args = {}

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
