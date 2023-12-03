from tools import FileInput,MultiFieldFormula

fileinput_6 = FileInput(
    base_dir = "One Tool At A Time - Testing/MultiFieldFormula",
    file_path = "C:/Users/Michael Michelini/Desktop/alt2py/tests/One Tool At A Time - Testing/OneToolData/PetStoreMonthlySales.avro",
).execute()

fileinput_6 = FileInput(
    base_dir = "One Tool At A Time - Testing/MultiFieldFormula",
    file_path = "C:/Users/Michael Michelini/Desktop/alt2py/tests/One Tool At A Time - Testing/OneToolData/PetStoreMonthlySales.avro",
).execute()

multifieldformula_36 = MultiFieldFormula(
    fields = ['NAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP'],
    expression = "Uppercase([_CurrentField_])",
    type = None,
    size = None,
).execute(fileinput_6)

multifieldformula_36 = MultiFieldFormula(
    fields = ['NAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP'],
    expression = "Uppercase([_CurrentField_])",
    type = None,
    size = None,
).execute(fileinput_6)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

multifieldformula_37 = MultiFieldFormula(
    fields = ['NAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP'],
    expression = "Uppercase([_CurrentField_])",
    type = None,
    size = None,
    prefix = "New_",
).execute(fileinput_6)

multifieldformula_37 = MultiFieldFormula(
    fields = ['NAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP'],
    expression = "Uppercase([_CurrentField_])",
    type = None,
    size = None,
    prefix = "New_",
).execute(fileinput_6)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

multifieldformula_38 = MultiFieldFormula(
    fields = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August ', 'September', 'October', 'November', 'December'],
    expression = "[_CurrentField_]/[Total ]*100",
    type = "FixedDecimal",
    size = "4.1",
    suffix = "% Total",
).execute(fileinput_6)

multifieldformula_38 = MultiFieldFormula(
    fields = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August ', 'September', 'October', 'November', 'December'],
    expression = "[_CurrentField_]/[Total ]*100",
    type = "FixedDecimal",
    size = "4.1",
    suffix = "% Total",
).execute(fileinput_6)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003
