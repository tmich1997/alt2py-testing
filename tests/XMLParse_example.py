from tools import FileInput,XMLParse,Sort

fileinput_285 = FileInput(
    base_dir = "One Tool At A Time - Testing/XMLParse",
    file_path = "../OneToolData/CustomerXML.avro",
).execute()

fileinput_285 = FileInput(
    base_dir = "One Tool At A Time - Testing/XMLParse",
    file_path = "../OneToolData/CustomerXML.avro",
).execute()

xmlparse_278 = XMLParse(
    field = "customer_xml",
    root = None,
    parse_children = True,
    ignore_errors = False,
).execute(fileinput_285)

xmlparse_278 = XMLParse(
    field = "customer_xml",
    root = None,
    parse_children = True,
    ignore_errors = False,
).execute(fileinput_285)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

xmlparse_286 = XMLParse(
    field = "customer_xml",
    root = None,
    return_outer = True,
    ignore_errors = False,
).execute(fileinput_285)

xmlparse_286 = XMLParse(
    field = "customer_xml",
    root = None,
    return_outer = True,
    ignore_errors = False,
).execute(fileinput_285)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

xmlparse_289 = XMLParse(
    field = "customer_xml",
    root = None,
    ignore_errors = False,
).execute(fileinput_285)

xmlparse_289 = XMLParse(
    field = "customer_xml",
    root = None,
    ignore_errors = False,
).execute(fileinput_285)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

xmlparse_292 = XMLParse(
    field = "customer_xml",
    root = "transactions",
    return_outer = True,
    ignore_errors = False,
).execute(fileinput_285)

xmlparse_292 = XMLParse(
    field = "customer_xml",
    root = "transactions",
    return_outer = True,
    ignore_errors = False,
).execute(fileinput_285)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005

xmlparse_295 = XMLParse(
    field = "customer_xml",
    root = "transaction",
    parse_children = True,
    ignore_errors = False,
).execute(fileinput_285)

xmlparse_295 = XMLParse(
    field = "customer_xml",
    root = "transaction",
    parse_children = True,
    ignore_errors = False,
).execute(fileinput_285)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007

xmlparse_298 = XMLParse(
    field = "customer_xml",
    root = None,
    auto_detect_root = True,
    parse_children = True,
    ignore_errors = False,
).execute(fileinput_285)

xmlparse_298 = XMLParse(
    field = "customer_xml",
    root = None,
    auto_detect_root = True,
    parse_children = True,
    ignore_errors = False,
).execute(fileinput_285)

# MISSING TOOL - Tool: DbFileOutput, id: 10009

# MISSING TOOL - Tool: DbFileOutput, id: 10009

sort_300 = Sort(
    fields = ['row_id'],
    orders = [False],
    maintain_order = True,
).execute(fileinput_285)

sort_300 = Sort(
    fields = ['row_id'],
    orders = [False],
    maintain_order = True,
).execute(fileinput_285)

xmlparse_301 = XMLParse(
    field = "customer_xml",
    root = None,
    auto_detect_root = True,
    parse_children = True,
    ignore_errors = False,
).execute(sort_300)

xmlparse_301 = XMLParse(
    field = "customer_xml",
    root = None,
    auto_detect_root = True,
    parse_children = True,
    ignore_errors = False,
).execute(sort_300)

# MISSING TOOL - Tool: DbFileOutput, id: 10011

# MISSING TOOL - Tool: DbFileOutput, id: 10011
