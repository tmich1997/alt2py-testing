import xml.etree.ElementTree as ET;
from functools import reduce;
import pandas as pd;
import shapely
import json;
import jsbeautifier;

from tools import (
    TextToColumns,
    GenerateRows,
    RegEx,
    Summarise,
    Formula,
    Clean,
    FileInput,
    Select,
    Join,
    MultiFieldFormula,
    MultiRowFormula,
    RecordID,
    SelectRecords,
    Sort,
    Unique,
    JoinMultiple,
    Union,
    Filter,
    CrossTab,
    Transpose,
    Sample,
    Impute,
    MultiFieldBin,
    OverSample,
    Tile,
    XMLParse,
    DateTime,
    FileInput,
    TextInput
)

tool_name_map = {
    "AppendFields":"Join",
    "DbFileInput":"FileInput",
    "TextInput":"TextInput",
    "DateTime":"DateTime",
    "TextToColumns":"TextToColumns",
    "RegEx":"RegEx",
    "XMLParse":"XMLParse",
    "Select":"Select",
    "GenerateRows":"GenerateRows",
    "Impute":"Impute",
    "MultiFieldBin":"MultiFieldBin",
    "OverSample":"OverSample",
    "Tile":"Tile",
    "Join":"Join",
    "Summarize":"Summarise",
    "Formula":"Formula",
    "Sample":"Sample",
    "Clean":"Clean",
    "MultiFieldFormula":"MultiFieldFormula",
    "MultiRowFormula":"MultiRowFormula",
    "RecordID":"RecordID",
    "RandomSample":"Sample",
    "SelectRecords":"SelectRecords",
    "Sort":"Sort",
    "Unique":"Unique",
    "JoinMultiple":"JoinMultiple",
    "Union":"Union",
    "Filter":"Filter",
    "CrossTab":"CrossTab",
    "Transpose":"Transpose",
}
executors = {
    "AppendFields":Join,
    "DbFileInput":FileInput,
    "TextInput":TextInput,
    "DateTime":DateTime,
    "TextToColumns":TextToColumns,
    "RegEx":RegEx,
    "XMLParse":XMLParse,
    "Select":Select,
    "GenerateRows":GenerateRows,
    "Impute":Impute,
    "MultiFieldBin":MultiFieldBin,
    "OverSample":OverSample,
    "Tile":Tile,
    "Join":Join,
    "Summarize":Summarise,
    "Formula":Formula,
    "Sample":Sample,
    "Clean":Clean,
    "MultiFieldFormula":MultiFieldFormula,
    "MultiRowFormula":MultiRowFormula,
    "RecordID":RecordID,
    "RandomSample":Sample,
    "SelectRecords":SelectRecords,
    "Sort":Sort,
    "Unique":Unique,
    "JoinMultiple":JoinMultiple,
    "Union":Union,
    "Filter":Filter,
    "CrossTab":CrossTab,
    "Transpose":Transpose,
}

class Tool:
    def __init__(self, id, name, xml, parent_dir):
        self.id = id
        self.name = name.split('.')
        self.xml = xml;
        self.dir = parent_dir;

        self.inputs = {};

        self.outputs = [];
        self.data = {}
        self.parsed = False;

        self.executor = self.add_executor();

    def get_input(self,to):
        oType = self.inputs[to].oType
        return self.inputs[to].origin.data[oType]

    def get_named_inputs(self,to):
        if isinstance(self.inputs[to],list):
            return [{
                        "name":c["name"],
                        "data":c["connection"].origin.data[c["connection"].oType]
                    } for c in self.inputs[to]]
        raise Except("Inputs not named. Use get input for unnamed connections")

    def add_executor(self):
        if self.name[-1] in executors:
            return lambda: executors[self.name[-1]](yxdb_tool = self)

    def execute(self):
        if self.executor:
            print("EXECUTING TOOL: "+self.id + " - " + self.name[-1])
            self.executor();
        else:
            print("Missing executor for: " + self.name[-1])

    def is_ready(self,parsing = False):
        print("ISREADY")
        ready = True;
        if parsing:
            print(self.inputs)
            for type,con in self.inputs.items():
                print(type,con)
                if isinstance(con, list):
                    for c in con:
                        ready = (ready and c["connection"].origin.parsed)
                else:
                    ready = (ready and con.origin.parsed)
        else:
            for type,con in self.inputs.items():
                if isinstance(con, list):
                    for c in con:
                        ready = (ready and c["connection"].oType in c["connection"].origin.data.keys())
                else:
                    ready = (ready and con.oType in con.origin.data.keys())
        return ready;

    def as_python(self):
        output_string = ""
        if self.name[-1] not in tool_name_map:
            output_string = f"# MISSING TOOL - Tool: {self.name[-1]}, id: {self.id}\n"
        else:
            tool = executors[self.name[-1]](yxdb_tool = self,execute = False)
            args = tool.config.get_required_kwargs()
            output_string = tool_name_map[self.name[-1]]+"(\n"
            for arg in args:
                value = arg["value"]
                opts = jsbeautifier.default_options()
                opts.indent_size = 4;
                opts.indent_level = 1;
                if isinstance(value,dict):
                    value = arg["key"] + " = " + str(value) + ",\n";
                    output_string += jsbeautifier.beautify(value, opts) + "\n";
                elif isinstance(value,str):
                    value = value.replace("\\","/")
                    if '"' in value and "'" in value:
                        value = '"""' + value + '"""';
                    elif '"' in value:
                        value = "'" + value + "'";
                    else:
                        value = '"' + value + '"';
                    value = arg["key"] + " = " + value+ ",\n";
                    output_string += jsbeautifier.beautify(value, opts) + "\n";
                else:
                    value = arg["key"] + " = " + str(value) + ",\n";
                    output_string += jsbeautifier.beautify(value, opts) + "\n";

            self.parsed = True;
            map = tool.get_yxdb_mapping();

            output_string += ")"

            input_var_string = ".execute("

            if map["Input"]:
                input_vars = []
                if isinstance(map["Input"],list):
                    for inp in map["Input"]:
                        origin_tool = self.inputs[inp].origin
                        input_vars.append(f"{tool_name_map[origin_tool.name[-1]]}_{str(origin_tool.id)}".lower())
                elif map["Input"]=="__named_inputs__":
                    input_list = []
                    for inp in self.inputs["Input"]:
                        origin_tool = inp["connection"].origin
                        input_list.append(f"{tool_name_map[origin_tool.name[-1]]}_{str(origin_tool.id)}".lower())
                    input_vars.append(f"[{','.join(input_list)}]")
                elif map["Input"] in self.inputs:
                    origin_tool = self.inputs[map["Input"]].origin
                    input_vars.append(f"{tool_name_map[origin_tool.name[-1]]}_{str(origin_tool.id)}".lower())

                input_var_string += f"{','.join(input_vars)})\n"
            else:
                input_var_string += ")\n"

            output_string +=input_var_string

            if map["Output"]:
                output_var_name = f"{tool_name_map[self.name[-1]]}_{str(self.id)}".lower()
                output_string = output_var_name + " = "+ output_string

        return output_string

class Connection:
    def __init__(self, start_tool, end_tool, start_connection, end_connection):
        self.origin = start_tool;
        self.destination = end_tool;
        self.oType = start_connection;
        self.dType = end_connection;

class Workflow:
    def __init__(self, filename):
        self.filename = filename
        self.roots = [];
        self.pot_solutions = [];
        self.pot_calc_solutions = [];
        self.parse_alteryx_workflow(filename)
        # self.parse_solution()

    def parse_alteryx_workflow(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        # Store all tool IDs that have inputs or outputs
        tool_ids = set()
        for connection in root.iter('Connection'):
            for anchor in connection:
                tool_ids.add(anchor.attrib.get('ToolID'))

        tools = {}

        # Create tools
        for node in root.iter('Node'):
            tool_id = node.attrib.get('ToolID')
            tool_name = None
            gui_settings = node.find('GuiSettings')
            if gui_settings is not None:
                tool_name = gui_settings.attrib.get('Plugin')
                if not tool_name:
                    map = {
                        "Cleanse":"Clean",
                        "Predictive Tools\Create_Samples":"Sample",
                        "SelectRecords":"SelectRecords",
                        "Imputation_v3":"Impute",
                        "MultiFieldBinning_v2":"MultiFieldBin",
                        "Predictive Tools\\Oversample_Field":"OverSample",
                        "RandomRecords":"RandomSample",
                    }
                    tool_name = map[node.find("EngineSettings").get("Macro").replace(".yxmc","")]
            # Skip adding tool if it has no inputs or outputs
            if tool_id not in tool_ids:
                continue;
            tool = Tool(tool_id, tool_name.replace("Alteryx",""), node, self.filename)
            tools[tool_id] = tool

        # Establish connections
        for connection in root.find("Connections").iter('Connection'):
            start_node_id = connection[0].attrib.get('ToolID')
            oType = connection[0].attrib.get('Connection')
            end_node_id = connection[1].attrib.get('ToolID')
            dType = connection[1].attrib.get('Connection')

            newConnection = Connection(
                tools[start_node_id],
                tools[end_node_id],
                oType,
                dType
            )

            con_name = connection.get("name")

            if con_name is not None:
                if dType not in tools[end_node_id].inputs:
                    tools[end_node_id].inputs[dType] = [{"name": con_name,"connection": newConnection}]
                else:
                    tools[end_node_id].inputs[dType].append({"name": con_name,"connection": newConnection})
            else:
                tools[end_node_id].inputs[dType] = newConnection

            tools[start_node_id].outputs.append(newConnection)

        for tool in tools:
            if len(tools[tool].inputs) == 0:
                self.roots.append(tools[tool])

    # def parse_solution(self):
    #     for root in self.roots:
    #         if len(root.outputs)==1 and root.outputs[0].destination.name[-1]=='BrowseV2':
    #             self.pot_solutions.append(root)

    def generate_python_script(self,file_name):
        roots = []+self.roots
        imports = []
        statements = []
        while len(roots) > 0:
            print(roots)
            i = 0;
            while not roots[i].is_ready(parsing=True):
                print(i)
                i+=1
            root = roots.pop(i)
            i-=1
            statements.append(root.as_python());

            if root.name[-1] in tool_name_map and tool_name_map[root.name[-1]] not in imports:
                imports.append(tool_name_map[root.name[-1]])
            statements.append(root.as_python());
            print("ROOT_ID ", root.id)

            new_roots = [];
            for con in root.outputs:
                if con.destination.is_ready(parsing=True) and con.destination.id not in [t.id for t in new_roots]:
                    new_roots.append(con.destination)
            print([r.id for r in new_roots])
            roots = roots[0:i+1] + new_roots + roots[i+1:]
            print([r.id for r in roots])
            print("loop")
        pyfile = ""
        if len(imports) > 3:
            pyfile = "from tools import (\n"
            for i in imports:
                pyfile += f"    {i},\n"
            pyfile = pyfile[:-3]
            pyfile += "\n)\n\n"
        else:
            pyfile = "from tools import " + ",".join(imports) + "\n\n"

        pyfile += "\n".join(statements)
        f = open(file_name, "w")
        f.write(pyfile)
        f.close()


    def execute_layer(self):
        old_roots = []
        for root in self.roots:
            root.execute();
            old_roots.append(root)

        self.create_next_layer();
        return old_roots

    def execute_wf(self):
        while(len(self.roots) > 0):
            self.execute_layer();

    def create_next_layer(self):
        new_roots = []
        for root in self.roots:
            for con in root.outputs:
                if con.destination.is_ready() and con.destination.id not in [t.id for t in new_roots]:
                    print("Tool: "+con.destination.id + " - " + con.destination.name[-1] + " is ready for execution")
                    new_roots.append(con.destination)

        old_roots = self.roots;
        self.roots = new_roots;

    def compare_tool_outputs(self,df1,df2):
        def find_mismatches(df1, df2):
            # Compare the two DataFrames element-wise
            comparison_result = df1 != df2

            # Find the rows and columns where mismatches occur
            rows_with_mismatches, columns_with_mismatches = (comparison_result).any(axis=1), (comparison_result).any(axis=0)

            # Extract the rows and columns with mismatches
            mismatched_rows = df1[rows_with_mismatches].index
            mismatched_columns = df1.columns[columns_with_mismatches]

            return mismatched_rows, mismatched_columns

        for col in df2:
            if df2[col].dtype=="float64":
                df2[col] = df2[col].astype(pd.Float64Dtype()).round(6)
                df1[col] = df1[col].astype(pd.Float64Dtype()).round(6)
        comp = df1 == df2
        both_na = df1.isna() & df2.isna()

        for col in df1:
            for i in range(len(df1[col])):
                if isinstance(df1[col][i], shapely.geometry.base.BaseGeometry):
                    comp.loc[i, col]=df1[col][i].equals(df2[col][i])

        passed = (comp |both_na).all(axis=None)

        if not passed:
            print(df1.columns)
            print(df2.columns)
            print(df1.dtypes)
            print(df2.dtypes)
            # Find the rows and columns with mismatches
            mismatched_rows, mismatched_columns = find_mismatches(df1, df2)
            # Print the result
            print(df1.loc[mismatched_rows])
            print(df1[mismatched_columns])
        else:
            return True

    def compare_solutions(self):
        for t1 in self.pot_solutions:
            for t2 in self.pot_calc_solutions:
                print(t1.data["Output"])
                print(t2)
                if self.compare_tool_outputs(t1.data["Output"],t2.data["Output"]):
                    print("PASSED: ",wf.filename)
