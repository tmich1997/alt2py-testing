from tools import FileInput,TextToColumns

fileinput_141 = FileInput(
    base_dir = "One Tool At A Time - Testing/TextToColumns",
    file_path = "../OneToolData/CustomerFileAddressesNarrow.avro",
).execute()

fileinput_141 = FileInput(
    base_dir = "One Tool At A Time - Testing/TextToColumns",
    file_path = "../OneToolData/CustomerFileAddressesNarrow.avro",
).execute()

texttocolumns_142 = TextToColumns(
    field = "Address",
    root_name = "Address",
    num_fields = 3,
).execute(fileinput_141)

texttocolumns_142 = TextToColumns(
    field = "Address",
    root_name = "Address",
    num_fields = 3,
).execute(fileinput_141)

texttocolumns_144 = TextToColumns(
    field = "Address3",
    root_name = "StateZip",
    num_fields = 3,
    delim = " -",
).execute(texttocolumns_142)

texttocolumns_144 = TextToColumns(
    field = "Address3",
    root_name = "StateZip",
    num_fields = 3,
    delim = " -",
).execute(texttocolumns_142)

# MISSING TOOL - Tool: DbFileOutput, id: 9998

# MISSING TOOL - Tool: DbFileOutput, id: 9998

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

fileinput_148 = FileInput(
    base_dir = "One Tool At A Time - Testing/TextToColumns",
    file_path = "../OneToolData/Alteryx Tool Metadata.avro",
).execute()

fileinput_148 = FileInput(
    base_dir = "One Tool At A Time - Testing/TextToColumns",
    file_path = "../OneToolData/Alteryx Tool Metadata.avro",
).execute()

texttocolumns_147 = TextToColumns(
    field = "Category_and_Search_Tags",
    root_name = "Category_and_Search_Tags",
    num_fields = 2,
    delim = "|",
    ign_brackets = True,
).execute(fileinput_148)

texttocolumns_147 = TextToColumns(
    field = "Category_and_Search_Tags",
    root_name = "Category_and_Search_Tags",
    num_fields = 2,
    delim = "|",
    ign_brackets = True,
).execute(fileinput_148)

texttocolumns_158 = TextToColumns(
    field = "Category_and_Search_Tags2",
    num_fields = 1,
    delim = "| []",
    ign_double_quote = True,
).execute(texttocolumns_147)

texttocolumns_158 = TextToColumns(
    field = "Category_and_Search_Tags2",
    num_fields = 1,
    delim = "| []",
    ign_double_quote = True,
).execute(texttocolumns_147)

# MISSING TOOL - Tool: DbFileOutput, id: 9996

# MISSING TOOL - Tool: DbFileOutput, id: 9996

texttocolumns_159 = TextToColumns(
    field = "Category_and_Search_Tags2",
    num_fields = 1,
    delim = "| []",
    ign_double_quote = True,
    skip_empty = True,
).execute(texttocolumns_147)

texttocolumns_159 = TextToColumns(
    field = "Category_and_Search_Tags2",
    num_fields = 1,
    delim = "| []",
    ign_double_quote = True,
    skip_empty = True,
).execute(texttocolumns_147)

# MISSING TOOL - Tool: DbFileOutput, id: 9995

# MISSING TOOL - Tool: DbFileOutput, id: 9995

# MISSING TOOL - Tool: DbFileOutput, id: 9997

# MISSING TOOL - Tool: DbFileOutput, id: 9997

fileinput_10007 = FileInput(
    base_dir = "One Tool At A Time - Testing/TextToColumns",
    file_path = "C:/Users/Michael Michelini/Desktop/alt2py/tests/One Tool At A Time - Testing/OneToolData/text_to_columns_custom.avro",
).execute()

fileinput_10007 = FileInput(
    base_dir = "One Tool At A Time - Testing/TextToColumns",
    file_path = "C:/Users/Michael Michelini/Desktop/alt2py/tests/One Tool At A Time - Testing/OneToolData/text_to_columns_custom.avro",
).execute()

texttocolumns_10002 = TextToColumns(
    field = "Field1",
    num_fields = 5,
    delim = " 	 -
        ",
).execute(fileinput_10007)

texttocolumns_10002 = TextToColumns(
    field = "Field1",
    num_fields = 5,
    delim = " 	 -
        ",
).execute(fileinput_10007)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005
