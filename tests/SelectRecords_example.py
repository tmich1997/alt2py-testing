from tools import FileInput,SelectRecords

fileinput_1 = FileInput(
    base_dir = "One Tool At A Time - Testing/SelectRecords",
    file_path = "../OneToolData/Merged_employees.avro",
).execute()

fileinput_1 = FileInput(
    base_dir = "One Tool At A Time - Testing/SelectRecords",
    file_path = "../OneToolData/Merged_employees.avro",
).execute()

selectrecords_10 = SelectRecords(
    conditions = ['-87', '109-113', '10800', '20000+'],
    index = 1,
).execute(fileinput_1)

selectrecords_10 = SelectRecords(
    conditions = ['-87', '109-113', '10800', '20000+'],
    index = 1,
).execute(fileinput_1)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

selectrecords_13 = SelectRecords(
    conditions = ['109-113'],
    index = 1,
).execute(fileinput_1)

selectrecords_13 = SelectRecords(
    conditions = ['109-113'],
    index = 1,
).execute(fileinput_1)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

selectrecords_15 = SelectRecords(
    conditions = ['10800'],
    index = 1,
).execute(fileinput_1)

selectrecords_15 = SelectRecords(
    conditions = ['10800'],
    index = 1,
).execute(fileinput_1)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

selectrecords_17 = SelectRecords(
    conditions = ['20000+'],
    index = 1,
).execute(fileinput_1)

selectrecords_17 = SelectRecords(
    conditions = ['20000+'],
    index = 1,
).execute(fileinput_1)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005
