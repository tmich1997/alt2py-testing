from tools import FileInput,Formula

fileinput_72 = FileInput(
    base_dir = "One Tool At A Time - Testing/Formula",
    file_path = "../OneToolData/CustomerFile2_Narrow.avro",
).execute()

fileinput_72 = FileInput(
    base_dir = "One Tool At A Time - Testing/Formula",
    file_path = "../OneToolData/CustomerFile2_Narrow.avro",
).execute()

formula_115 = Formula(
    formulae = [{
        'field': 'RecordSource',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': '"Alteryx Sample Data"'
    }],
).execute(fileinput_72)

formula_115 = Formula(
    formulae = [{
        'field': 'RecordSource',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': '"Alteryx Sample Data"'
    }],
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

formula_116 = Formula(
    formulae = [{
        'field': 'Region',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': 'IF [Latitude] > 39.7 \nTHEN "North" \nELSE "South"\nENDIF'
    }],
).execute(fileinput_72)

formula_116 = Formula(
    formulae = [{
        'field': 'Region',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': 'IF [Latitude] > 39.7 \nTHEN "North" \nELSE "South"\nENDIF'
    }],
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

formula_117 = Formula(
    formulae = [{
        'field': 'City_titleCase',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': 'Titlecase([City])'
    }],
).execute(fileinput_72)

formula_117 = Formula(
    formulae = [{
        'field': 'City_titleCase',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': 'Titlecase([City])'
    }],
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

formula_118 = Formula(
    formulae = [{
        'field': 'City',
        'type': 'String',
        'size': '256',
        'expression': 'Titlecase([City])'
    }],
).execute(fileinput_72)

formula_118 = Formula(
    formulae = [{
        'field': 'City',
        'type': 'String',
        'size': '256',
        'expression': 'Titlecase([City])'
    }],
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005

formula_119 = Formula(
    formulae = [{
        'field': 'RecordSource',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': '"Alteryx Sample Data"'
    }, {
        'field': 'Region',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': 'IF [Latitude] > 39.7 \nTHEN "North" \nELSE "South"\nENDIF'
    }, {
        'field': 'City',
        'type': 'String',
        'size': '256',
        'expression': 'Titlecase([City])'
    }],
).execute(fileinput_72)

formula_119 = Formula(
    formulae = [{
        'field': 'RecordSource',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': '"Alteryx Sample Data"'
    }, {
        'field': 'Region',
        'type': 'V_WString',
        'size': '1073741823',
        'expression': 'IF [Latitude] > 39.7 \nTHEN "North" \nELSE "South"\nENDIF'
    }, {
        'field': 'City',
        'type': 'String',
        'size': '256',
        'expression': 'Titlecase([City])'
    }],
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007

formula_120 = Formula(
    formulae = [{
        'field': 'AverageSpendPerVisit',
        'type': 'FixedDecimal',
        'size': '19.2',
        'expression': 'ROUND([Spend]/[Visits],1)'
    }],
).execute(fileinput_72)

formula_120 = Formula(
    formulae = [{
        'field': 'AverageSpendPerVisit',
        'type': 'FixedDecimal',
        'size': '19.2',
        'expression': 'ROUND([Spend]/[Visits],1)'
    }],
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10009

# MISSING TOOL - Tool: DbFileOutput, id: 10009

formula_121 = Formula(
    formulae = [{
        'field': 'AverageSpendPerVisit',
        'type': 'FixedDecimal',
        'size': '19.2',
        'expression': '[Spend]/[Visits]'
    }, {
        'field': 'AverageSpendPerVisit',
        'type': 'FixedDecimal',
        'size': '19.2',
        'expression': 'ROUND([AverageSpendPerVisit], 1)'
    }],
).execute(fileinput_72)

formula_121 = Formula(
    formulae = [{
        'field': 'AverageSpendPerVisit',
        'type': 'FixedDecimal',
        'size': '19.2',
        'expression': '[Spend]/[Visits]'
    }, {
        'field': 'AverageSpendPerVisit',
        'type': 'FixedDecimal',
        'size': '19.2',
        'expression': 'ROUND([AverageSpendPerVisit], 1)'
    }],
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10011

# MISSING TOOL - Tool: DbFileOutput, id: 10011
