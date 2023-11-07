import pandas as pd;
import numpy as np;
from natsort import natsort_keygen;
from tools.RecordID import RecordID

class CrossJoin:
    def __init__(self,xml=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        self.xml = xml;
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);
        elif kwargs:
            self.load_json(kwargs);


    def load_json(self,kwargs):
        c = self.config;

        c.fields = kwargs["fields"] if "fields" in kwargs else c.fields



    def load_xml(self,xml):
        c = self.config;

    def get_renames(self,left_df,right_df):
        renames = {}
        renames_back = {}
        for i, name1 in enumerate(left_df.columns):
            for j, name2 in enumerate(right_df.columns):
                if name1 == name2:
                    renames[name2] = "Source_"+name2
                    renames_back["Source_"+name2] = name2

        return (renames,renames_back)

    def execute(self,left_datasource,right_datasource):
        c = self.config;

        left_df = left_datasource.copy();
        right_df = right_datasource.copy();

        renames,renames_back = self.get_renames(left_df,right_df);

        print(renames,renames_back)

        if len(renames):
            right_df.rename(columns = renames, inplace=True)

        raise Exception("HERE")


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
