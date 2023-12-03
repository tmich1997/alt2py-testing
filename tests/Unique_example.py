from tools import FileInput,Unique,Sort

fileinput_10003 = FileInput(
    base_dir = "One Tool At A Time - Testing/Unique",
    file_path = "../OneToolData/CustomerFile_duplicates.avro",
).execute()

fileinput_10003 = FileInput(
    base_dir = "One Tool At A Time - Testing/Unique",
    file_path = "../OneToolData/CustomerFile_duplicates.avro",
).execute()

unique_8 = Unique(
    fields = ['FirstName', 'LastName'],
).execute(fileinput_10003)

unique_8 = Unique(
    fields = ['FirstName', 'LastName'],
).execute(fileinput_10003)

sort_10006 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(unique_8)

sort_10006 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(unique_8)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

sort_10007 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(unique_8)

sort_10007 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(unique_8)

# MISSING TOOL - Tool: DbFileOutput, id: 10004

# MISSING TOOL - Tool: DbFileOutput, id: 10004

unique_11 = Unique(
    fields = ['FirstName', 'LastName', 'Address'],
).execute(fileinput_10003)

unique_11 = Unique(
    fields = ['FirstName', 'LastName', 'Address'],
).execute(fileinput_10003)

sort_10008 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(unique_11)

sort_10008 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(unique_11)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

sort_10009 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(unique_11)

sort_10009 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(unique_11)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005
