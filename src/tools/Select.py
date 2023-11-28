import pandas as pd;
import numpy as np;

dtype_map = {
    "Bool":pd.BooleanDtype(),
    "Byte":np.bytes_,
    "Int16":pd.Int64Dtype(),
    "Int32":pd.Int64Dtype(),
    "Int64":pd.Int64Dtype(),
    "FixedDecimal":pd.Float64Dtype(),
    "Double":pd.Float64Dtype(),
    "String":pd.StringDtype(),
    "WString":pd.StringDtype(),
    "V_String":pd.StringDtype(),
    "V_WString":pd.StringDtype(),
    "Date":'datetime64[ns]',
    "Time":'datetime64[ns]',
    "DateTime":'datetime64[ns]',
    "SpatialObj":'geometry'
}

class Select:
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
        c.reorder = xml.find(".//Configuration/OrderChanged").get("value")=="True"
        c.keep_unknown = xml.find(".//SelectField[@field='*Unknown']").get("selected")=="True"

        for field in xml.findall(".//SelectField"):
            if field.get('field') == "*Unknown":
                continue;

            current_field = field.get('field')
            selected = field.get('selected')=='True'

            if selected:
                c.selected.append(current_field)
                if 'rename' in field.attrib:
                    c.renames[current_field] = field.get('rename')
                if 'type' in field.attrib:
                    c.types[current_field] = field.get('type')
            else:
                c.deselected.append(current_field)

    def execute(self,input_datasource):
        c = self.config
        df = input_datasource.copy();
        fields = [];
        if c.keep_unknown:
            fields = [] if not c.reorder else c.selected
            for f in df.columns:
                if f not in c.deselected and (f not in c.selected or not c.reorder):
                    fields.append(f)
        else:
            fields = c.selected

        for fld in c.types:
            if c.types[fld] =="SpatialObj":
                continue
            df[fld] = df[fld].astype(dtype_map[c.types[fld]])

        df = df.loc[:, fields]
        df.rename(columns=c.renames,inplace=True)
        return df

    class Config:
        def __init__(
            self
        ):
            self.selected = [];
            self.deselected = [];
            self.keep_unknown = False;
            self.types = {};
            self.renames = {};
            self.reorder = True;


        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
