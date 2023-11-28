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
    #PARSE CONFIGURATION
    # df = tool.get_input("Input")
    # next_df = TextToColumns(xml=tool.xml).execute(df)
    # tool.data["Output"] = next_df
    TextToColumns(yxdb_tool = tool)

def execute_RegEx(tool):
    #PARSE CONFIGURATION
    df = tool.get_input("Input")
    next_df = RegEx(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_Formula(tool):
    #PARSE CONFIGURATION
    df = tool.get_input("Input")
    print("HERE")
    print(df.dtypes)
    next_df = Formula(xml=tool.xml).execute(df)
    print(next_df.dtypes)
    tool.data["Output"] = next_df

def execute_Summarize(tool):
    #PARSE CONFIGURATION
    df = tool.get_input("Input")
    next_df = Summarise(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df


def execute_Select(tool):
    #PARSE CONFIGURATION
    df = tool.get_input("Input")
    next_df = Select(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df


def execute_GenerateRows(tool):
    if len(tool.inputs)>0:
        df = tool.get_input("Input")
        next_df = GenerateRows(xml=tool.xml).execute(df)
    else:
        next_df = GenerateRows(xml=tool.xml).execute()

    tool.data["Output"] = next_df

def execute_Join(tool):
    left = tool.get_input("Left")
    right = tool.get_input("Right")
    out = Join(xml=tool.xml).execute(left,right)

    tool.data["Left"] = out.left
    tool.data["Join"] = out.inner
    tool.data["Right"] = out.right


def execute_MultiFieldFormula(tool):
    df = tool.get_input("Input")
    next_df = MultiFieldFormula(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df


def execute_MultiRowFormula(tool):
    df = tool.get_input("Input")
    next_df = MultiRowFormula(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_RecordID(tool):
    df = tool.get_input("Input")
    next_df = RecordID(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_SelectRecords(tool):
    df = tool.get_input("Input")
    next_df = SelectRecords(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_Sort(tool):
    df = tool.get_input("Input")
    next_df = Sort(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df


def execute_Unique(tool):
    df = tool.get_input("Input")
    out = Unique(xml=tool.xml).execute(df)

    tool.data["Unique"] = out.unique
    tool.data["Duplicates"] = out.duplicates

def execute_JoinMultiple(tool):
    dfs = tool.get_named_inputs("Input")
    next_df = JoinMultiple(xml=tool.xml).execute(dfs)
    tool.data["Output"] = next_df

def execute_Union(tool):
    dfs = tool.get_named_inputs("Input")
    ##TODO: rework the logic of how inputs are passed to exec. don't use dict, use list.
    next_df = Union(xml=tool.xml).execute(dfs)
    tool.data["Output"] = next_df

def execute_Filter(tool):
    df = tool.get_input("Input")
    out = Filter(xml=tool.xml).execute(df)
    tool.data["True"] = out.true
    tool.data["False"] = out.false

def execute_CrossTab(tool):
    df = tool.get_input("Input")
    next_df = CrossTab(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_Transpose(tool):
    df = tool.get_input("Input")
    next_df = Transpose(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_Clean(tool):
    df = tool.get_input("Input2")
    next_df = Clean(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_Sample(tool):
    df = tool.get_input("Input")
    out = Sample(xml=tool.xml).execute(df)

    tool.data["Estimation"] = out.train
    tool.data["Validation"] = out.validate
    tool.data["Holdout"] = out.hold

def execute_Impute(tool):
    df = tool.get_input("Input")
    next_df = Impute(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_MultiFieldBin(tool):
    df = tool.get_input("Input")
    next_df = MultiFieldBin(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_OverSample(tool):
    df = tool.get_input("Input")
    next_df = OverSample(xml=tool.xml).execute(df)
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

def execute_Tile(tool):
    df = tool.get_input("Input")
    next_df = Tile(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_XMLParse(tool):
    df = tool.get_input("Input")
    next_df = XMLParse(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_DateTime(tool):
    df = tool.get_input("Input")
    next_df = DateTime(xml=tool.xml).execute(df)
    tool.data["Output"] = next_df

def execute_AppendFields(tool):
    left = tool.get_input("Targets")
    right = tool.get_input("Source")

    next_df = Join(xml=tool.xml).execute(left,right)
    tool.data["Output"] = next_df


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
