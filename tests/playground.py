import sys
sys.path.append('../src')
from tools.ReadYXDB import Workflow

wf_paths = {
    "Sample":"\\Sample",
    "OverSample":"\OverSample",
    "RandomSample":"\RandomSample",
    "Clean":"\\Clean",
    "Filter":"\\Filter",
    "Formula":"\Formula",
    "GenerateRows":"\Generate_Rows",
    "Impute":"\Impute",
    "MultiFieldBin":"\MultiFieldBin",
    "MultiFieldFormula":"\MultiFieldFormula",
    "MultiRowFormula":"\MultiRowFormula",
    "RecordID":"\RecordID",
    "Select":"\Select",
    "SelectRecords":"\SelectRecords",
    "Sort":"\Sort",
    "Unique":"\\Unique",
    "Tile":"\\Tile",

    "Join":"\Join",
    # "JoinMultiple":"\\JoinMultiple",
    "Union":"\\Union",
    "AppendFields":"\\AppendFields",

    "Summarize":"\Summarize",
    "CrossTab":"\\CrossTab",
    "Transpose":"\\Transpose",

    "DateTime":"\DateTime",
    "TextToColumns":"\Text_To_Columns",
    "RegEx":"\RegEx",
    "XMLParse":"\XMLParse",
}

def convert_test(test_name):
    print("\n"*20 + test_name)
    folder_path = ".\\One Tool At A Time - Testing\\" + test_name
    workflow_yxmd = folder_path + wf_paths[test_name] + "_edit.yxmd";
    workflow = Workflow(workflow_yxmd).generate_python_script(test_name+"_example.py")

for k in wf_paths:
    convert_test(k)

# convert_test("AppendFields")
