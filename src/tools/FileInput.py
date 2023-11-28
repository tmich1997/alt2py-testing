import pandas as pd;
import fastavro;
import json;
import os;
os.environ['USE_PYGEOS'] = '0';
import geopandas as gpd;
from shapely.geometry import shape;

dtype_map = {
    "avro_string":pd.StringDtype(),
    "avro_int":pd.Int32Dtype(),
    "avro_long":pd.Int64Dtype(),
    "avro_float":pd.Float32Dtype(),
    "avro_double":pd.Float64Dtype(),
    "avro_boolean":pd.BooleanDtype()
}


class FileInput:
    def __init__(self,xml=None,json=None,config=None,file_name=None):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            print("XML")
            self.load_xml(xml)
        elif json:
            print("JSON")
            self.load_json(json);
        elif file_name:
            print("FILENAME")
            self.load_filename(file_name);

    def load_filename(self,file_name):
        self.config.file_name = file_name
        self.config.file_type = file_name.split(".")[-1]

    def set_dir(self,dir):
        self.config.dir = dir
        return self

    def load_xml(self,xml):
        c = self.config
        config = xml.find("Properties").find("Configuration");
        file = config.find("File");
        c.file_name = file.text
        c.file_type = c.file_name.split(".")[-1]


    def read_avro(self):
        from pathlib import Path
        print(Path.cwd())
        print(self.config.file_name)
        with open(self.config.file_name, 'rb') as f:
            reader = fastavro.reader(f);
            schema = reader.schema;
            column_names = [field["name"] for field in schema["fields"]];
            data = []
            for record in reader:
                data.append(record);
        # Convert the list of records to a pandas DataFrame
        data_df = pd.DataFrame(data,columns=[c["name"] for c in schema["fields"]]);
        for col in schema["fields"]:
            typ = self.config.file_type + "_"
            if isinstance(col["type"], list):
               typ += col["type"][1]
            else:
               typ += col["type"]

            data_df[col["name"]] = data_df[col["name"]].astype(dtype_map[typ], errors='ignore')
            if typ==self.config.file_type +"_string":
                is_na = pd.isna(data_df[col["name"]])
                is_json = (data_df[col["name"]].str.startswith("{") & data_df[col["name"]].str.endswith("}")).all() and not is_na.all()
                is_date = (is_na | data_df[col["name"]].str.match(r'\d{4}-\d{2}-\d{2}( \d{2}:\d{2}:\d{2})*')).all() and (not is_na.all())
                # is_time = (is_na | data_df[col["name"]].str.match(r'\d{2}:\d{2}:\d{2}')).all() and (not is_na.all())

                if is_json:
                    geometry = [shape(json.loads(x)) for x in data_df[col["name"]]]
                    data_df[col["name"]] = geometry
                    data_df = gpd.GeoDataFrame(data_df, geometry=col["name"],crs='EPSG:4326')
                    continue

                if is_date:
                    data_df[col["name"]] = pd.to_datetime(data_df[col["name"]])
                    continue

                data_df[col["name"]] = data_df[col["name"]].astype(pd.StringDtype())

                # if is_time:
                #     data_df[col["name"]] = pd.to_datetime("1900-01-01 " +data_df[col["name"]])
                #     continue

        return data_df;

    def auto_dtype(self,df):
        for column in df.columns:
            if df[column].dtype in ('float64','int64'):
                continue
            is_bytes_df = df[column].apply(lambda x: isinstance(x, bytes))
            is_na = pd.isna(df[column])
            is_num_not_na = pd.to_numeric(df[column], errors='coerce').notna()
            is_numeric = (is_num_not_na | is_na).all() and (not is_na.all()) and (is_num_not_na.any())
            is_float = df[column].str.contains("\.",na=False).any()

            if is_numeric:
                if not is_float:
                    df[column] = df[column].astype(pd.Int64Dtype())
                else:
                    df[column] = df[column].astype(pd.Float64Dtype())
                continue

            is_json = (df[column].str.startswith("{") & df[column].str.endswith("}")).all() and not is_na.all()

            if is_json:
                geometry = [shape(json.loads(x)) for x in df[column]]
                df[column] = geometry
                gdf = gpd.GeoDataFrame(df, geometry=column,crs='EPSG:4326')
                continue

            na_map = df[column].isna()
            date_map = df[column].str.match(r'\d{4}-\d{2}-\d{2}( \d{2}:\d{2}:\d{2})*')
            int_map = df[column].str.match(r'^\d+[\.]*\d+$')

            is_date = (not na_map.all()) and (na_map | date_map).all()
            is_int = (not na_map.all()) and (na_map | int_map).all()
            if is_date:
                # If all values have the 'yyyy-mm-dd' format, convert the column to datetime
                df[column] = pd.to_datetime(df[column])
                continue
            df[column] = df[column].astype(pd.StringDtype())

            # is_time = (is_na | df[column].str.match(r'\d{2}:\d{2}:\d{2}')).all() and (not is_na.all())
            # if is_time:
            #     df[column] = pd.to_datetime("1900-01-01 " +df[column])
            #     continue

        return df

    def read_csv(self):
        c = self.config;
        return self.auto_dtype(pd.read_csv(c.file_name))

    def execute(self,input_datasource=None):
        c = self.config
        new_df = None
        if c.dir:
            print(c.dir,c.file_name)
            new_path = os.path.join(c.dir,"..\\", c.file_name)
            # Normalize the path to handle any '..' or '.' segments. if C.file_name is a full path, it will ignore the rest.
            new_path = os.path.normpath(new_path)
            print(new_path)
            c.file_name = new_path
        if c.file_type=="avro":
            new_df = self.read_avro()
        if c.file_type=="csv":
            new_df = self.read_csv()

        return new_df

    class Config:
        def __init__(
            self,
            file_name = None,
        ):
            self.dir = None;
            if file_name:
                self.file_name = file_name;
                self.file_type = file_name.split(".")[-1];
            else:
                self.file_name = None;
                self.file_type = None;


        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out

# FileInput(file_name="../One Tool At A Time - Testing/OneToolData/SpatialFile1.avro").execute()
