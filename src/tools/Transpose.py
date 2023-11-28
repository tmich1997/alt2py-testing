import pandas as pd;
from tools.Sort import Sort

class Transpose:
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
        c.sort=True;
        c.key_fields = [f.get("field") for f in xml.find(".//Configuration//KeyFields")]
        c.data_fields = []
        for f in xml.find(".//Configuration//DataFields"):
            if f.get("selected")=="True" and f.get("field")!="*Unknown":
                c.data_fields.append(f.get("field"))

    def execute(self,input_datasource):
        c = self.config;
        new_df = input_datasource.copy()

        if c.drop_unknown:
            new_df = new_df[c.key_fields + c.data_fields]

        dtypes_of_values = set(new_df[c.data_fields].dtypes.tolist())

        new_df = pd.melt(new_df, id_vars=c.key_fields, var_name=c.var_name, value_name=c.value_name)

        field_order_mapping = {month: i+1 for i, month in enumerate(c.data_fields)}

        new_df = new_df.sort_values(by=c.var_name, key=lambda x: x.map(field_order_mapping)).reset_index(drop=True)
        new_df.index.name = "__INDEX__"
        new_df = new_df.sort_values(by=c.key_fields+["__INDEX__"]).reset_index(drop=True)
        new_df.index.name = None

        new_df[c.var_name] = new_df[c.var_name].astype(pd.StringDtype())
        if len(dtypes_of_values)>1:
            is_numeric_result = input_datasource[c.data_fields].applymap(pd.api.types.is_numeric_dtype).all().all()
            if is_numeric_result:
                new_df[c.value_name] = new_df[c.value_name].astype(pd.Float64Dtype())
            else:
                new_df[c.value_name] = new_df[c.value_name].astype(pd.StringDtype())
        # if len(dtypes_of_values)==1:
        #     new_df[c.value_name] = new_df[c.value_name].astype(dtypes_of_values[0])
        return new_df

    class Config:
        def __init__(
            self
        ):
            self.key_fields = []
            self.data_fields = []
            self.drop_unknown = True;
            self.var_name = "Name"
            self.value_name = "Value"
            self.sort = False;

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
