from tools import FileInput,Select

fileinput_72 = FileInput(
    base_dir = "One Tool At A Time - Testing/Select",
    file_path = "../OneToolData/CustomerFile3.avro",
).execute()

fileinput_72 = FileInput(
    base_dir = "One Tool At A Time - Testing/Select",
    file_path = "../OneToolData/CustomerFile3.avro",
).execute()

select_74 = Select(
    selected = ['CustomerID', 'FirstName', 'LastName'],
    reorder = False,
).execute(fileinput_72)

select_74 = Select(
    selected = ['CustomerID', 'FirstName', 'LastName'],
    reorder = False,
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

select_75 = Select(
    selected = ['Visits'],
    keep_unknown = True,
    reorder = False,
    change_types = {
        'Visits': 'Int16'
    },
).execute(fileinput_72)

select_75 = Select(
    selected = ['Visits'],
    keep_unknown = True,
    reorder = False,
    change_types = {
        'Visits': 'Int16'
    },
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10000

# MISSING TOOL - Tool: DbFileOutput, id: 10000

select_76 = Select(
    selected = ['CustomerID', 'Spend', 'Visits', 'StoreNumber', 'FirstName', 'LastName', 'Address', 'CustomerSegment', 'SpatialObj', 'Latitude', 'Longitude'],
    deselected = ['City', 'State', 'ZIP', 'Zip4'],
    keep_unknown = True,
    renames = {
        'CustomerID': 'Customer ID',
        'Spend': 'Total Spent',
        'Visits': 'Total Visits',
        'StoreNumber': 'Store Number'
    },
).execute(fileinput_72)

select_76 = Select(
    selected = ['CustomerID', 'Spend', 'Visits', 'StoreNumber', 'FirstName', 'LastName', 'Address', 'CustomerSegment', 'SpatialObj', 'Latitude', 'Longitude'],
    deselected = ['City', 'State', 'ZIP', 'Zip4'],
    keep_unknown = True,
    renames = {
        'CustomerID': 'Customer ID',
        'Spend': 'Total Spent',
        'Visits': 'Total Visits',
        'StoreNumber': 'Store Number'
    },
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

select_77 = Select(
    selected = ['Address', 'City', 'CustomerID', 'CustomerSegment', 'FirstName', 'LastName', 'Latitude', 'Longitude', 'SpatialObj', 'Spend', 'State', 'StoreNumber', 'Visits', 'ZIP', 'Zip4'],
    keep_unknown = True,
).execute(fileinput_72)

select_77 = Select(
    selected = ['Address', 'City', 'CustomerID', 'CustomerSegment', 'FirstName', 'LastName', 'Latitude', 'Longitude', 'SpatialObj', 'Spend', 'State', 'StoreNumber', 'Visits', 'ZIP', 'Zip4'],
    keep_unknown = True,
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10002

# MISSING TOOL - Tool: DbFileOutput, id: 10002

select_81 = Select(
    selected = ['FirstName', 'LastName', 'Address', 'City', 'State', 'ZIP', 'Zip4', 'Visits', 'Spend'],
    keep_unknown = True,
    reorder = False,
    renames = {
        'FirstName': 'CustomerFirstName',
        'LastName': 'CustomerLastName',
        'Address': 'CustomerAddress',
        'City': 'CustomerCity',
        'State': 'CustomerState',
        'ZIP': 'CustomerZIP',
        'Zip4': 'CustomerZip4',
        'Visits': 'CustomerVisits',
        'Spend': 'CustomerSpend'
    },
).execute(fileinput_72)

select_81 = Select(
    selected = ['FirstName', 'LastName', 'Address', 'City', 'State', 'ZIP', 'Zip4', 'Visits', 'Spend'],
    keep_unknown = True,
    reorder = False,
    renames = {
        'FirstName': 'CustomerFirstName',
        'LastName': 'CustomerLastName',
        'Address': 'CustomerAddress',
        'City': 'CustomerCity',
        'State': 'CustomerState',
        'ZIP': 'CustomerZIP',
        'Zip4': 'CustomerZip4',
        'Visits': 'CustomerVisits',
        'Spend': 'CustomerSpend'
    },
).execute(fileinput_72)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003
