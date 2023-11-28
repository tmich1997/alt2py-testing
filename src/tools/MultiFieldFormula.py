import pandas as pd;
import numpy as np;
from tools.Formula import Functions,Formula
from tools.Select import dtype_map

class MultiFieldFormula:
    def __init__(self,xml=None,json=None,config=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);

    def load_xml(self,xml):
        c = self.config;

        c.expression =  xml.find(".//Configuration/Expression").text

        fields =  xml.find(".//Configuration/Fields")

        c.fields = []

        for f in fields:
            if not f.get("selected")=="False" and not f.get("name")=="*Unknown":
                c.fields.append(f.get("name"))

        change_type =  xml.find(".//Configuration/ChangeFieldType").get("value")=="True"

        if change_type:
            out = xml.find(".//Configuration/OutputFieldType")
            c.type = out.get("type");
            if out.get("size"):
                c.size = out.get("size");
                if out.get("scale"):
                    c.size+="."+out.get("scale")

        add_fields = xml.find(".//Configuration/CopyOutput").get("value")=="True"

        if add_fields:
            is_prefix =  xml.find(".//Configuration/NewFieldAddOnPos").text=="Prefix"
            if is_prefix:
                c.prefix = xml.find(".//Configuration/NewFieldAddOn").text;
            else:
                c.suffix = xml.find(".//Configuration/NewFieldAddOn").text;

    def execute(self,input_datasource):
        c = self.config
        df = input_datasource.copy();

        tool = Formula();

        for f in c.fields:
            expression =  Functions.format_field_formula(c.expression,f)
            tool.add_formula(field=c.prefix +f+c.suffix,expression=Functions.format_field_formula(c.expression,f),type=c.type,size=c.size)

        next_df = tool.execute(df)
        return next_df

    class Config:
        def __init__(
            self
        ):
            self.fields = []
            self.expression = None
            self.type = False
            self.size = None;
            self.prefix = ''
            self.suffix = ''


        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
