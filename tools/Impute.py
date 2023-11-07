import pandas as pd;
import re
from tools.Summarise import Aggregators as Agg

class Impute:
    def __init__(self,xml=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);
        elif kwargs:
            self.load_json(kwargs);


# <Configuration>
# <Value name="listbox Select Incoming Fields">"item_id","2012_sales","2013_sales","2014_sales"</Value>
# <Value name="radio Null Value">True</Value>
# <Value name="radio User Specified Replace From Value">False</Value>
# <Value name="updown User Replace Value">0.00000</Value>
# <Value name="radio Mean">False</Value>
# <Value name="radio Median">False</Value>
# <Value name="radio Mode">False</Value>
# <Value name="radio User Specified Replace With Value">True</Value>
# <Value name="updown User Replace With Value">0.00000</Value>
# <Value name="checkbox Impute Indicator">False</Value>
# <Value name="checkbox Imputed Values Separate Field">False</Value>
# </Configuration>

    def load_json(self,json):
        c = self.config;

    def load_xml(self,xml):
        c = self.config;
        values = {v.get("name"):v.text for v in xml.find(".//Configuration")}

        print(values)

        c.fields = re.sub('^\"|\"$',"",values["listbox Select Incoming Fields"]).split('","')
        c.impute_values = pd.NA if values["radio Null Value"]=="True" else values["updown User Replace Value"]
        c.impute_fn = "Avg" if values["radio Mean"]=="True" else "Median"  if values["radio Median"]=="True" else "Mode" if values["radio Mode"]=="True" else False;
        c.impute_static = values["updown User Replace With Value"] if not c.impute_fn else False
        c.indicator = values["checkbox Impute Indicator"]=="True"
        c.add_fields = values["checkbox Imputed Values Separate Field"]=="True"
        c.new_suffix = "_ImputedValue"
        c.indicator_suffix = "_Indicator"

    def execute(self,input_datasource):
        c = self.config;

        new_df = input_datasource.copy()
        print(c)

        if c.impute_fn:
            replacement = new_df[c.fields].apply(Agg.get_by_name(c.impute_fn))
            print(replacement)
        else:
            is_int = any(["Int" in str(new_df[f].dtype) for f in c.fields])
            replacement = int(c.impute_static.split(".")[0]) if is_int else float(c.impute_static)

        if c.indicator:
            indicators = new_df[c.fields] == replacement
            indicators.columns = [c.indicator_prefix + col + c.indicator_suffix for col in indicators.columns]
            new_df = pd.concat([new_df,indicators],axis=1)

        if c.add_fields:
            print("HERE")
            print(new_df)
            added_df = new_df[c.fields].replace({pd.NA:replacement})
            print(added_df)
            added_df.columns = [c.new_prefix + col + c.new_suffix for col in added_df.columns]
            print(added_df)
            new_df = pd.concat([new_df,added_df],axis=1)
            print(new_df)
        else:
            new_df[c.fields] = new_df[c.fields].replace({pd.NA:replacement}).astype(new_df[c.fields].dtypes)

        return new_df.reset_index(drop=True)

    class Config:
        def __init__(
            self
        ):
            self.fields=[];
            self.impute_values=pd.NA;
            self.impute_fn = "Average";
            self.impute_static = False;
            self.indicator = False;
            self.add_fields = False;
            self.new_prefix = ""
            self.new_suffix = ""
            self.indicator_prefix = ""
            self.indicator_suffix = ""

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
