import pandas as pd;
import numpy as np;
from natsort import natsort_keygen;
from tools.RecordID import RecordID

class Sort:
    def __init__(self,yxdb_tool=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        if config:
            self.config = config
        elif yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        elif json:
            self.load_json(json);
        elif kwargs:
            self.load_json(kwargs);


    def load_json(self,kwargs):
        c = self.config;

        c.fields = kwargs["fields"] if "fields" in kwargs else c.fields
        c.orders = kwargs["orders"] if "orders" in kwargs else [True]*len(kwargs["fields"])
        c.handle_alpha_numeric = kwargs["handle_alpha_numeric"] if "handle_alpha_numeric" in kwargs else c.handle_alpha_numeric
        c.na_position = kwargs["na_position"] if "na_position" in kwargs else c.na_position
        c.maintain_order = kwargs["maintain_order"] if "maintain_order" in kwargs else c.maintain_order


    def load_yxdb_tool(self,tool,execute=True):
        c = self.config;
        xml = tool.xml

        fields = xml.find(".//Configuration//SortInfo")
        c.handle_alpha_numeric = fields.get("locale")!="0"
        for f in fields:
            c.fields.append(f.get("field"))
            c.orders.append(f.get("order")=="Ascending")
        c.maintain_order = True;
        if execute:
            df = tool.get_input("Input")
            next_df = self.execute(df)
            tool.data["Output"] = next_df

    def execute(self,input_datasource):
        c = self.config;
        new_df = input_datasource.copy();
        if c.maintain_order:
            new_df = RecordID(field="__record_id__").execute(new_df)
            c.fields +=["__record_id__"]
            c.orders +=[True]

        if c.handle_alpha_numeric:
            new_df = new_df.sort_values(
                by=c.fields,
                ascending=c.orders,
                key=lambda x: natsort_keygen()(x.replace({pd.NA: None if c.na_position=="first" else "zzzzzzzzzzzzzzzzzzzzz"})),
            )
        else:
            new_df = new_df.sort_values(by=c.fields, ascending=c.orders, na_position=c.na_position)

        if c.maintain_order:
            new_df = new_df.drop("__record_id__", axis=1)
            c.fields.pop()
            c.orders.pop()

        return new_df.reset_index(drop=True)

    class Config:
        def __init__(
            self
        ):
            self.fields=[];
            self.orders=[]
            self.handle_alpha_numeric = False;
            self.na_position = "first"
            self.maintain_order = False;

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
