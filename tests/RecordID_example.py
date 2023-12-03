from tools import TextInput,RecordID

textinput_123 = TextInput(
    columns = {
        'CustomerID': ['49', '456', '31', '5', '1', '2'],
        'FirstName': ['Thomas', 'Galileo', 'Benjamin', 'Dorothy', 'Louis', 'Tim'],
        'LastName': ['Edison', None, 'Franklin', 'Gerber', 'Pasteur', 'Berners-Lee'],
        'Gender': ['M', 'M', 'M', 'F', 'M', 'M'],
        'JoinDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2014-10-01', '2013-09-06', '2014-01-26'],
        'Region': ['South', 'South', 'Midwest', 'Northeast', 'West', 'Midwest']
    },
).execute()

textinput_123 = TextInput(
    columns = {
        'CustomerID': ['49', '456', '31', '5', '1', '2'],
        'FirstName': ['Thomas', 'Galileo', 'Benjamin', 'Dorothy', 'Louis', 'Tim'],
        'LastName': ['Edison', None, 'Franklin', 'Gerber', 'Pasteur', 'Berners-Lee'],
        'Gender': ['M', 'M', 'M', 'F', 'M', 'M'],
        'JoinDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2014-10-01', '2013-09-06', '2014-01-26'],
        'Region': ['South', 'South', 'Midwest', 'Northeast', 'West', 'Midwest']
    },
).execute()

recordid_124 = RecordID(
    field = "Record ID",
    type = "Int64",
    position_first = True,
).execute(textinput_123)

recordid_124 = RecordID(
    field = "Record ID",
    type = "Int64",
    position_first = True,
).execute(textinput_123)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

recordid_125 = RecordID(
    field = "Record ID Last Column",
    start = -100,
    type = "Int32",
).execute(textinput_123)

recordid_125 = RecordID(
    field = "Record ID Last Column",
    start = -100,
    type = "Int32",
).execute(textinput_123)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

recordid_136 = RecordID(
    field = "Record ID Last Column",
    start = -100,
    type = "String",
).execute(textinput_123)

recordid_136 = RecordID(
    field = "Record ID Last Column",
    start = -100,
    type = "String",
).execute(textinput_123)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003
