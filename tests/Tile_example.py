from tools import (
    FileInput,
    Tile,
    Select,
    Formul
)

fileinput_17 = FileInput(
    base_dir = "One Tool At A Time - Testing/Tile",
    file_path = "../OneToolData/Address_Sale_Data_Narrow.avro",
).execute()

fileinput_17 = FileInput(
    base_dir = "One Tool At A Time - Testing/Tile",
    file_path = "../OneToolData/Address_Sale_Data_Narrow.avro",
).execute()

tile_18 = Tile(
    mode = "records",
    num_tiles = 5,
).execute(fileinput_17)

tile_18 = Tile(
    mode = "records",
    num_tiles = 5,
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

tile_19 = Tile(
    mode = "sum",
    field = "AVERAGE SALE",
    num_tiles = 5,
).execute(fileinput_17)

tile_19 = Tile(
    mode = "sum",
    field = "AVERAGE SALE",
    num_tiles = 5,
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

tile_21 = Tile(
    mode = "smart",
    field = "AVERAGE SALE",
).execute(fileinput_17)

tile_21 = Tile(
    mode = "smart",
    field = "AVERAGE SALE",
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

tile_24 = Tile(
    mode = "manual",
    field = "AVERAGE SALE",
).execute(fileinput_17)

tile_24 = Tile(
    mode = "manual",
    field = "AVERAGE SALE",
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005

tile_27 = Tile(
    mode = "unique",
    field = ['STATE', 'ZIP'],
).execute(fileinput_17)

tile_27 = Tile(
    mode = "unique",
    field = ['STATE', 'ZIP'],
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007

tile_29 = Tile(
    mode = "records",
    num_tiles = 5,
).execute(fileinput_17)

tile_29 = Tile(
    mode = "records",
    num_tiles = 5,
).execute(fileinput_17)

# MISSING TOOL - Tool: DbFileOutput, id: 10009

# MISSING TOOL - Tool: DbFileOutput, id: 10009

select_10012 = Select(
    selected = ['AVERAGE SALE'],
    keep_unknown = True,
    reorder = False,
    change_types = {
        'AVERAGE SALE': 'Double'
    },
).execute(fileinput_17)

select_10012 = Select(
    selected = ['AVERAGE SALE'],
    keep_unknown = True,
    reorder = False,
    change_types = {
        'AVERAGE SALE': 'Double'
    },
).execute(fileinput_17)

formula_10011 = Formula(
    formulae = [{
        'field': 'AVERAGE SALE',
        'type': 'Double',
        'size': '8',
        'expression': 'iif([AVERAGE SALE]==55,Null(),[AVERAGE SALE] - 20)'
    }],
).execute(select_10012)

formula_10011 = Formula(
    formulae = [{
        'field': 'AVERAGE SALE',
        'type': 'Double',
        'size': '8',
        'expression': 'iif([AVERAGE SALE]==55,Null(),[AVERAGE SALE] - 20)'
    }],
).execute(select_10012)

tile_10010 = Tile(
    mode = "smart",
    field = "AVERAGE SALE",
).execute(formula_10011)

tile_10010 = Tile(
    mode = "smart",
    field = "AVERAGE SALE",
).execute(formula_10011)

# MISSING TOOL - Tool: DbFileOutput, id: 10013

# MISSING TOOL - Tool: DbFileOutput, id: 10013
