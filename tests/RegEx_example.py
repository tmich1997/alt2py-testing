from tools import FileInput,RegEx

fileinput_17 = FileInput(
    base_dir = "One Tool At A Time - Testing/RegEx",
    file_path = "../OneToolData/CustomerFileAddressesNarrow.avro",
).execute()

fileinput_17 = FileInput(
    base_dir = "One Tool At A Time - Testing/RegEx",
    file_path = "../OneToolData/CustomerFileAddressesNarrow.avro",
).execute()

regex_12 = RegEx(
    field = "Address",
    pattern = "-(/d{4})",
    method = "parse",
    replace_pattern = None,
    root_name = None,
    num_fields = None,
    new_fields = [{
        'field': 'zip4',
        'type': 'String',
        'size': '4'
    }],
).execute(fileinput_17)

regex_12 = RegEx(
    field = "Address",
    pattern = "-(/d{4})",
    method = "parse",
    replace_pattern = None,
    root_name = None,
    num_fields = None,
    new_fields = [{
        'field': 'zip4',
        'type': 'String',
        'size': '4'
    }],
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

regex_15 = RegEx(
    field = "Address",
    pattern = ".*-/d{4}",
    replace_pattern = None,
    root_name = None,
    num_fields = None,
    new_fields = [{
        'field': 'has_zip4'
    }],
).execute(fileinput_17)

regex_15 = RegEx(
    field = "Address",
    pattern = ".*-/d{4}",
    replace_pattern = None,
    root_name = None,
    num_fields = None,
    new_fields = [{
        'field': 'has_zip4'
    }],
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005

regex_18 = RegEx(
    field = "Name",
    pattern = "([a-z]+)/s([a-z]+)",
    method = "parse",
    replace_pattern = None,
    root_name = None,
    num_fields = None,
    new_fields = [{
        'field': 'First Name',
        'type': 'String',
        'size': '128'
    }, {
        'field': 'Last Name',
        'type': 'String',
        'size': '128'
    }],
).execute(fileinput_17)

regex_18 = RegEx(
    field = "Name",
    pattern = "([a-z]+)/s([a-z]+)",
    method = "parse",
    replace_pattern = None,
    root_name = None,
    num_fields = None,
    new_fields = [{
        'field': 'First Name',
        'type': 'String',
        'size': '128'
    }, {
        'field': 'Last Name',
        'type': 'String',
        'size': '128'
    }],
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007

regex_1 = RegEx(
    field = "Address",
    pattern = "(.*),(.*),(.*)/s(/d{5})(-/d{4})?",
    method = "replace",
    replace_pattern = "$4: $2, $3",
    copy_unmatched = True,
    root_name = None,
    num_fields = None,
    new_fields = None,
).execute(fileinput_17)

regex_1 = RegEx(
    field = "Address",
    pattern = "(.*),(.*),(.*)/s(/d{5})(-/d{4})?",
    method = "replace",
    replace_pattern = "$4: $2, $3",
    copy_unmatched = True,
    root_name = None,
    num_fields = None,
    new_fields = None,
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

regex_10012 = RegEx(
    field = "Address",
    pattern = "[^,]+",
    method = "tokenize",
    replace_pattern = None,
    to_rows = True,
    root_name = None,
    num_fields = None,
    new_fields = None,
).execute(fileinput_17)

regex_10012 = RegEx(
    field = "Address",
    pattern = "[^,]+",
    method = "tokenize",
    replace_pattern = None,
    to_rows = True,
    root_name = None,
    num_fields = None,
    new_fields = None,
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10011

# MISSING TOOL - Tool: DbFileOutput, id: 10011

regex_8 = RegEx(
    field = "Address",
    pattern = "[^,]+",
    method = "tokenize",
    replace_pattern = None,
    root_name = "Address",
    num_fields = 3,
    on_error = "Warn",
    new_fields = None,
).execute(fileinput_17)

regex_8 = RegEx(
    field = "Address",
    pattern = "[^,]+",
    method = "tokenize",
    replace_pattern = None,
    root_name = "Address",
    num_fields = 3,
    on_error = "Warn",
    new_fields = None,
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001
