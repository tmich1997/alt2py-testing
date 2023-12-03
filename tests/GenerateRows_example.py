from tools import GenerateRows,TextInput

generaterows_151 = GenerateRows(
    field = "RowCount",
    field_type = "Int32",
    initialiser = "1",
    on_loop = "RowCount + 1",
    should_loop = "RowCount <= 10",
).execute()

generaterows_151 = GenerateRows(
    field = "RowCount",
    field_type = "Int32",
    initialiser = "1",
    on_loop = "RowCount + 1",
    should_loop = "RowCount <= 10",
).execute()

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

textinput_160 = TextInput(
    columns = {
        'customer_id': ['1', '2', '3', '4', '5'],
        'account_no': ['10545321', '56193802', '64266537', '13829101', '17735208'],
        'acct_limit': ['10000', '2500', '1500', '5000', '20000'],
        'authorized_users': ['2', '1', '3', '0', '2'],
        'accountOpenDt': ['2015-02-01', '2015-05-04', '2015-06-11', '2015-08-20', '2015-10-31'],
        'accountCloseDt': ['2015-02-07', '2015-05-07', '2015-06-11', '2015-09-03', '2015-11-01']
    },
).execute()

textinput_160 = TextInput(
    columns = {
        'customer_id': ['1', '2', '3', '4', '5'],
        'account_no': ['10545321', '56193802', '64266537', '13829101', '17735208'],
        'acct_limit': ['10000', '2500', '1500', '5000', '20000'],
        'authorized_users': ['2', '1', '3', '0', '2'],
        'accountOpenDt': ['2015-02-01', '2015-05-04', '2015-06-11', '2015-08-20', '2015-10-31'],
        'accountCloseDt': ['2015-02-07', '2015-05-07', '2015-06-11', '2015-09-03', '2015-11-01']
    },
).execute()

generaterows_159 = GenerateRows(
    field = "Authorized_UserNo",
    field_type = "Int32",
    initialiser = "1",
    on_loop = "Authorized_UserNo + 1",
    should_loop = "Authorized_UserNo <= [authorized_users]",
).execute(textinput_160)

generaterows_159 = GenerateRows(
    field = "Authorized_UserNo",
    field_type = "Int32",
    initialiser = "1",
    on_loop = "Authorized_UserNo + 1",
    should_loop = "Authorized_UserNo <= [authorized_users]",
).execute(textinput_160)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

generaterows_153 = GenerateRows(
    field = "Authorized_UserNo",
    field_type = "Int32",
    initialiser = "1",
    on_loop = "Authorized_UserNo + 1",
    should_loop = "authorized_UserNo <= 3",
).execute(textinput_160)

generaterows_153 = GenerateRows(
    field = "Authorized_UserNo",
    field_type = "Int32",
    initialiser = "1",
    on_loop = "Authorized_UserNo + 1",
    should_loop = "authorized_UserNo <= 3",
).execute(textinput_160)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

generaterows_168 = GenerateRows(
    field = "date",
    field_type = "Date",
    initialiser = "[accountOpenDt]",
    on_loop = 'DateTimeAdd([date],1,"days")',
    should_loop = "[date]<=[accountCloseDt]",
).execute(textinput_160)

generaterows_168 = GenerateRows(
    field = "date",
    field_type = "Date",
    initialiser = "[accountOpenDt]",
    on_loop = 'DateTimeAdd([date],1,"days")',
    should_loop = "[date]<=[accountCloseDt]",
).execute(textinput_160)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007

generaterows_10009 = GenerateRows(
    field = "customer_id",
    mode = "update",
    field_type = None,
    initialiser = "1",
    on_loop = "[customer_id] + 1",
    should_loop = "[customer_id] <= [authorized_users]",
).execute(textinput_160)

generaterows_10009 = GenerateRows(
    field = "customer_id",
    mode = "update",
    field_type = None,
    initialiser = "1",
    on_loop = "[customer_id] + 1",
    should_loop = "[customer_id] <= [authorized_users]",
).execute(textinput_160)

# MISSING TOOL - Tool: DbFileOutput, id: 10010

# MISSING TOOL - Tool: DbFileOutput, id: 10010

textinput_165 = TextInput(
    columns = {
        'ItemID': ['1', '2', '3', '4', '5'],
        'category': ['A', 'A', 'B', 'A', 'B'],
        'minValue': ['10', '20', '2', '80', '3'],
        'maxValue': ['40', '20', '5', '120', '4']
    },
).execute()

textinput_165 = TextInput(
    columns = {
        'ItemID': ['1', '2', '3', '4', '5'],
        'category': ['A', 'A', 'B', 'A', 'B'],
        'minValue': ['10', '20', '2', '80', '3'],
        'maxValue': ['40', '20', '5', '120', '4']
    },
).execute()

generaterows_164 = GenerateRows(
    field = "whatIfTestValue",
    field_type = "Int32",
    initialiser = "[maxValue]",
    on_loop = "If [category]='A' Then [whatIfTestValue] - 10
    ElseIf[category] = 'B'
    Then[whatIfTestValue] - 1

    Else[minValue] - 1 // If an unknown category appears, this logic forces the next value to be less than the minValue, so that the loop stops.

    EndIf ",
    should_loop = "[whatIfTestValue] >= [minValue]",
).execute(textinput_165)

generaterows_164 = GenerateRows(
    field = "whatIfTestValue",
    field_type = "Int32",
    initialiser = "[maxValue]",
    on_loop = "If [category]='A' Then [whatIfTestValue] - 10
    ElseIf[category] = 'B'
    Then[whatIfTestValue] - 1

    Else[minValue] - 1 // If an unknown category appears, this logic forces the next value to be less than the minValue, so that the loop stops.

    EndIf ",
    should_loop = "[whatIfTestValue] >= [minValue]",
).execute(textinput_165)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005
