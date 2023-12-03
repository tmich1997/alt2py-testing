from tools import (
    TextInput,
    GenerateRows,
    Formula,
    Join,
    Filte
)

textinput_155 = TextInput(
    columns = {
        'CustomerID': ['49', '456', '31', '5', '1', '2'],
        'FirstName': ['Thomas', 'Galileo', 'Benjamin', 'Dorothy', 'Louis', 'Tim'],
        'LastName': ['Edison', None, 'Franklin', 'Gerber', 'Pasteur', 'Berners-Lee'],
        'Gender': ['M', 'M', 'M', 'F', 'M', 'M'],
        'Region': ['South', 'South', 'Midwest', 'Northeast', 'West', 'Midwest'],
        'Score': ['2', '1', '1', '22', '4', 'a']
    },
).execute()

textinput_155 = TextInput(
    columns = {
        'CustomerID': ['49', '456', '31', '5', '1', '2'],
        'FirstName': ['Thomas', 'Galileo', 'Benjamin', 'Dorothy', 'Louis', 'Tim'],
        'LastName': ['Edison', None, 'Franklin', 'Gerber', 'Pasteur', 'Berners-Lee'],
        'Gender': ['M', 'M', 'M', 'F', 'M', 'M'],
        'Region': ['South', 'South', 'Midwest', 'Northeast', 'West', 'Midwest'],
        'Score': ['2', '1', '1', '22', '4', 'a']
    },
).execute()

generaterows_157 = GenerateRows(
    field = "JoinDate",
    field_type = "Date",
    initialiser = 'DateTimeFormat(DateTimeNow(),"%Y-%m-%d")',
    on_loop = 'DateTimeAdd([JoinDate],1,"days")',
    should_loop = '[JoinDate]<=DateTimeAdd(DateTimeFormat(DateTimeNow(),"%Y-%m-%d"),5,"Days")

    ',
).execute()

generaterows_157 = GenerateRows(
    field = "JoinDate",
    field_type = "Date",
    initialiser = 'DateTimeFormat(DateTimeNow(),"%Y-%m-%d")',
    on_loop = 'DateTimeAdd([JoinDate],1,"days")',
    should_loop = '[JoinDate]<=DateTimeAdd(DateTimeFormat(DateTimeNow(),"%Y-%m-%d"),5,"Days")

    ',
).execute()

formula_158 = Formula(
    formulae = [{
        'field': 'FirstPurchaseDate',
        'type': 'Date',
        'size': '10',
        'expression': 'DateTimeAdd([JoinDate],-RandInt(15),"days")'
    }],
).execute(generaterows_157)

formula_158 = Formula(
    formulae = [{
        'field': 'FirstPurchaseDate',
        'type': 'Date',
        'size': '10',
        'expression': 'DateTimeAdd([JoinDate],-RandInt(15),"days")'
    }],
).execute(generaterows_157)

join_174 = Join(
    how = "position",
).execute(textinput_155,formula_158)

join_174 = Join(
    how = "position",
).execute(textinput_155,formula_158)

filter_143 = Filter(
    expression = "[CustomerID] > 30",
).execute(join_174)

filter_143 = Filter(
    expression = "[CustomerID] > 30",
).execute(join_174)

# MISSING TOOL - Tool: DbFileOutput, id: 161

# MISSING TOOL - Tool: DbFileOutput, id: 161

# MISSING TOOL - Tool: DbFileOutput, id: 162

# MISSING TOOL - Tool: DbFileOutput, id: 162

filter_142 = Filter(
    expression = "!IsNull([LastName])",
).execute(join_174)

filter_142 = Filter(
    expression = "!IsNull([LastName])",
).execute(join_174)

# MISSING TOOL - Tool: DbFileOutput, id: 163

# MISSING TOOL - Tool: DbFileOutput, id: 163

# MISSING TOOL - Tool: DbFileOutput, id: 164

# MISSING TOOL - Tool: DbFileOutput, id: 164

filter_139 = Filter(
    expression = '[JoinDate] <= ToDate(DateTimeAdd(DateTimeToday(), 1, "days"))',
).execute(join_174)

filter_139 = Filter(
    expression = '[JoinDate] <= ToDate(DateTimeAdd(DateTimeToday(), 1, "days"))',
).execute(join_174)

# MISSING TOOL - Tool: DbFileOutput, id: 165

# MISSING TOOL - Tool: DbFileOutput, id: 165

# MISSING TOOL - Tool: DbFileOutput, id: 166

# MISSING TOOL - Tool: DbFileOutput, id: 166

filter_152 = Filter(
    expression = '[JoinDate] <= ToDate(
    DateTimeAdd(DateTimeToday(), 2, "days")
    ) AND
        [JoinDate] >= DateTimeToday()
    ',
).execute(join_174)

filter_152 = Filter(
    expression = '[JoinDate] <= ToDate(
    DateTimeAdd(DateTimeToday(), 2, "days")
    ) AND
        [JoinDate] >= DateTimeToday()
    ',
).execute(join_174)

# MISSING TOOL - Tool: DbFileOutput, id: 167

# MISSING TOOL - Tool: DbFileOutput, id: 167

# MISSING TOOL - Tool: DbFileOutput, id: 168

# MISSING TOOL - Tool: DbFileOutput, id: 168

filter_141 = Filter(
    expression = "[JoinDate]>=[FirstPurchaseDate]",
).execute(join_174)

filter_141 = Filter(
    expression = "[JoinDate]>=[FirstPurchaseDate]",
).execute(join_174)

# MISSING TOOL - Tool: DbFileOutput, id: 169

# MISSING TOOL - Tool: DbFileOutput, id: 169

# MISSING TOOL - Tool: DbFileOutput, id: 171

# MISSING TOOL - Tool: DbFileOutput, id: 171

filter_140 = Filter(
    expression = '[Region]=="South"
    OR
    REGEX_Match(UPPERCASE([Region]), ".*WEST")
    ',
).execute(join_174)

filter_140 = Filter(
    expression = '[Region]=="South"
    OR
    REGEX_Match(UPPERCASE([Region]), ".*WEST")
    ',
).execute(join_174)

# MISSING TOOL - Tool: DbFileOutput, id: 172

# MISSING TOOL - Tool: DbFileOutput, id: 172

# MISSING TOOL - Tool: DbFileOutput, id: 173

# MISSING TOOL - Tool: DbFileOutput, id: 173
