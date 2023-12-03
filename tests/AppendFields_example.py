from alt2py.tools import FileInput,Formula,Join

fileinput_13 = FileInput(
    base_dir = "One Tool At A Time - Testing/AppendFields",
    file_path = "../OneToolData/State Populations.csv",
).execute()

fileinput_13 = FileInput(
    base_dir = "One Tool At A Time - Testing/AppendFields",
    file_path = "../OneToolData/State Populations.csv",
).execute()

fileinput_14 = FileInput(
    base_dir = "One Tool At A Time - Testing/AppendFields",
    file_path = "../OneToolData/Consumer_Segments.avro",
).execute()

fileinput_14 = FileInput(
    base_dir = "One Tool At A Time - Testing/AppendFields",
    file_path = "../OneToolData/Consumer_Segments.avro",
).execute()

formula_20 = Formula(
    formulae = [{
        'field': 'State',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': '[Customer Segment]'
    }],
).execute(fileinput_14)

formula_20 = Formula(
    formulae = [{
        'field': 'State',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': '[Customer Segment]'
    }],
).execute(fileinput_14)

join_1 = Join(
    how = "cross",
).execute(fileinput_13,formula_20)

join_1 = Join(
    how = "cross",
).execute(fileinput_13,formula_20)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

join_19 = Join(
    how = "cross",
).execute(formula_20,fileinput_13)

join_19 = Join(
    how = "cross",
).execute(formula_20,fileinput_13)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001
