import pandas as pd;

from tools.TextToColumns import TextToColumns
from tools.GenerateRows import GenerateRows
from tools.RegEx import RegEx
from tools.Summarise import Summarise
from tools.Formula import Formula
from tools.Clean import Clean
from tools.FileInput import FileInput
from tools.Select import Select
from tools.Join import Join
from tools.MultiFieldFormula import MultiFieldFormula
from tools.MultiRowFormula import MultiRowFormula
from tools.RecordID import RecordID
from tools.SelectRecords import SelectRecords
from tools.Sort import Sort
from tools.Unique import Unique
from tools.JoinMultiple import JoinMultiple
from tools.Union import Union
from tools.Filter import Filter
from tools.CrossTab import CrossTab
from tools.Transpose import Transpose
from tools.Sample import Sample
from tools.Impute import Impute
from tools.MultiFieldBin import MultiFieldBin
from tools.OverSample import OverSample
from tools.Tile import Tile
from tools.XMLParse import XMLParse
from tools.DateTime import DateTime

def execute_DbFileInput(tool, file_name=None):
    if file_name:
        next_df = FileInput(file_name=file_name).execute()
    else:
        next_df = FileInput(xml=tool.xml).set_dir(tool.dir).execute()
    if file_name:
        return next_df;
    tool.data["Output"] = next_df;

def execute_TextInput(tool):
    if tool.name[-1]=="TextInput":
        config = tool.xml.find("Properties").find("Configuration")
        fields = config.find("Fields")
        data = config.find("Data")

        field_names = []
        column_arrays = {}

        for field in fields:
            name = field.get("name");
            field_names.append(name);
            column_arrays[name] = []

        # Populate the arrays with the data values
        for row in data:
            for i,col in enumerate(row):
                column_arrays[field_names[i]].append(col.text)

        df = pd.DataFrame(column_arrays)
        df = handle_dtypes(df)
        tool.data["Output"] = df

def handle_dtypes(df,infer=True):
    for column in df.columns:
        is_bytes_df = df[column].apply(lambda x: isinstance(x, bytes))
        is_na = pd.isna(df[column])
        is_num_not_na = pd.to_numeric(df[column], errors='coerce').notna()
        is_numeric = (is_num_not_na | is_na).all() and (not is_na.all()) and (is_num_not_na.any())

        if is_numeric and infer:
            is_float = df[column].str.contains("\.",na=False).any()
            if not is_float:
                df[column] = df[column].astype(pd.Int64Dtype())
            else:
                df[column] = df[column].astype(pd.Float64Dtype())
            continue
        elif is_numeric:
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

def execute_TextToColumns(tool):
    TextToColumns(yxdb_tool = tool)

def execute_RegEx(tool):
    #PARSE CONFIGURATION
    RegEx(yxdb_tool = tool)

def execute_Formula(tool):
    #PARSE CONFIGURATION
    Formula(yxdb_tool = tool)

def execute_Summarize(tool):
    #PARSE CONFIGURATION
    Summarise(yxdb_tool = tool)


def execute_Select(tool):
    #PARSE CONFIGURATION
    Select(yxdb_tool = tool)

def execute_GenerateRows(tool):
    GenerateRows(yxdb_tool = tool)

def execute_Join(tool):
    Join(yxdb_tool = tool)

def execute_MultiFieldFormula(tool):
    MultiFieldFormula(yxdb_tool = tool)

def execute_MultiRowFormula(tool):
    MultiRowFormula(yxdb_tool = tool)

def execute_RecordID(tool):
    RecordID(yxdb_tool = tool)

def execute_SelectRecords(tool):
    SelectRecords(yxdb_tool = tool)

def execute_Sort(tool):
    Sort(yxdb_tool = tool)

def execute_Unique(tool):
    Unique(yxdb_tool = tool)

def execute_Union(tool):
    Union(yxdb_tool = tool)

def execute_Filter(tool):
    Filter(yxdb_tool = tool)

def execute_CrossTab(tool):
    CrossTab(yxdb_tool = tool)

def execute_Transpose(tool):
    Transpose(yxdb_tool = tool)

def execute_Clean(tool):
    Clean(yxdb_tool = tool)

def execute_Sample(tool):
    Sample(yxdb_tool = tool)

def execute_Impute(tool):
    Impute(yxdb_tool = tool)

def execute_MultiFieldBin(tool):
    MultiFieldBin(yxdb_tool = tool)

def execute_OverSample(tool):
    OverSample(yxdb_tool = tool)

def execute_Tile(tool):
    Tile(yxdb_tool = tool)

def execute_XMLParse(tool):
    XMLParse(yxdb_tool = tool)

def execute_DateTime(tool):
    DateTime(yxdb_tool = tool)

def execute_AppendFields(tool):
    left = tool.get_input("Targets")
    right = tool.get_input("Source")

    next_df = Join(xml=tool.xml).execute(left,right)
    tool.data["Output"] = next_df

def execute_JoinMultiple(tool):
    dfs = tool.get_named_inputs("Input")
    next_df = JoinMultiple(xml=tool.xml).execute(dfs)
    tool.data["Output"] = next_df

def execute_RandomSample(tool):
    df = tool.get_input("Input")
    #This logic doesn't warrant an entire new tool, so just do the parsing here.
    values = {v.get("name"):v.text for v in tool.xml.find(".//Configuration")}

    asNumber = values["Number"]=="True";
    asPercent = values["Percent"]=="True"
    seed = int(values["Seed"]) if values["Deterministic"]=="True" else None;
    train = int(values["NNumber"]) if asNumber else int(values["NPercent"])/100 if asPercent else None;

    if train is None:
        raise Exception("No train value")

    out = Sample(train=train,seed=seed).execute(df)
    tool.data["Output"] = out.train

executors = {
    "AppendFields":execute_AppendFields,
    "DbFileInput":execute_DbFileInput,
    "TextInput":execute_TextInput,
    "DateTime":execute_DateTime,
    "TextToColumns":execute_TextToColumns,
    "RegEx":execute_RegEx,
    "XMLParse":execute_XMLParse,
    "Select":execute_Select,
    "GenerateRows":execute_GenerateRows,
    "Impute":execute_Impute,
    "MultiFieldBin":execute_MultiFieldBin,
    "OverSample":execute_OverSample,
    "Tile":execute_Tile,
    "Join":execute_Join,
    "Summarize":execute_Summarize,
    "Formula":execute_Formula,
    "Sample":execute_Sample,
    "Clean":execute_Clean,
    "MultiFieldFormula":execute_MultiFieldFormula,
    "MultiRowFormula":execute_MultiRowFormula,
    "RecordID":execute_RecordID,
    "RandomSample":execute_RandomSample,
    "SelectRecords":execute_SelectRecords,
    "Sort":execute_Sort,
    "Unique":execute_Unique,
    "JoinMultiple":execute_JoinMultiple,
    "Union":execute_Union,
    "Filter":execute_Filter,
    "CrossTab":execute_CrossTab,
    "Transpose":execute_Transpose,
}
