from tools import FileInput,Summarise

fileinput_152 = FileInput(
    base_dir = "One Tool At A Time - Testing/Summarize",
    file_path = "../OneToolData/CustomerFile4.avro",
).execute()

fileinput_152 = FileInput(
    base_dir = "One Tool At A Time - Testing/Summarize",
    file_path = "../OneToolData/CustomerFile4.avro",
).execute()

summarise_111 = Summarise(
    fields = [{
        'field': 'Spend',
        'action': 'Avg',
        'name': 'Avg_Spend',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Median',
        'name': 'Median_Spend',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Mode',
        'name': 'Mode_Spend',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'StdDev',
        'name': 'StdDev_Spend',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Variance',
        'name': 'Variance_Spend',
        'props': {}
    }],
).execute(fileinput_152)

summarise_111 = Summarise(
    fields = [{
        'field': 'Spend',
        'action': 'Avg',
        'name': 'Avg_Spend',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Median',
        'name': 'Median_Spend',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Mode',
        'name': 'Mode_Spend',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'StdDev',
        'name': 'StdDev_Spend',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Variance',
        'name': 'Variance_Spend',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10013

# MISSING TOOL - Tool: DbFileOutput, id: 10013

summarise_103 = Summarise(
    fields = [{
        'field': 'ZIP',
        'action': 'First',
        'name': 'First_ZIP',
        'props': {}
    }, {
        'field': 'ZIP',
        'action': 'Last',
        'name': 'Last_ZIP',
        'props': {}
    }],
).execute(fileinput_152)

summarise_103 = Summarise(
    fields = [{
        'field': 'ZIP',
        'action': 'First',
        'name': 'First_ZIP',
        'props': {}
    }, {
        'field': 'ZIP',
        'action': 'Last',
        'name': 'Last_ZIP',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10011

# MISSING TOOL - Tool: DbFileOutput, id: 10011

summarise_77 = Summarise(
    fields = [{
        'field': 'State',
        'action': 'GroupBy',
        'name': 'State',
        'props': {}
    }, {
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }, {
        'field': 'Visits',
        'action': 'Median',
        'name': 'Median_Visits',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Sum',
        'name': 'Sum_Spend',
        'props': {}
    }],
).execute(fileinput_152)

summarise_77 = Summarise(
    fields = [{
        'field': 'State',
        'action': 'GroupBy',
        'name': 'State',
        'props': {}
    }, {
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }, {
        'field': 'Visits',
        'action': 'Median',
        'name': 'Median_Visits',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Sum',
        'name': 'Sum_Spend',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

summarise_75 = Summarise(
    fields = [{
        'field': 'FirstName',
        'action': 'Concat',
        'name': 'Concat_FirstName',
        'props': {
            'Concat_Start': '<',
            'Separator': '>,<',
            'Concat_End': '>'
        }
    }, {
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }],
).execute(fileinput_152)

summarise_75 = Summarise(
    fields = [{
        'field': 'FirstName',
        'action': 'Concat',
        'name': 'Concat_FirstName',
        'props': {
            'Concat_Start': '<',
            'Separator': '>,<',
            'Concat_End': '>'
        }
    }, {
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

summarise_91 = Summarise(
    fields = [{
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }, {
        'field': 'City',
        'action': 'Count',
        'name': 'Count',
        'props': {}
    }],
).execute(fileinput_152)

summarise_91 = Summarise(
    fields = [{
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }, {
        'field': 'City',
        'action': 'Count',
        'name': 'Count',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005

summarise_139 = Summarise(
    fields = [{
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }],
).execute(fileinput_152)

summarise_139 = Summarise(
    fields = [{
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10017

# MISSING TOOL - Tool: DbFileOutput, id: 10017

summarise_143 = Summarise(
    fields = [{
        'field': 'CustomerID',
        'action': 'Count',
        'name': 'Count',
        'props': {}
    }],
).execute(fileinput_152)

summarise_143 = Summarise(
    fields = [{
        'field': 'CustomerID',
        'action': 'Count',
        'name': 'Count',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10019

# MISSING TOOL - Tool: DbFileOutput, id: 10019

summarise_85 = Summarise(
    fields = [{
        'field': 'JoinDate',
        'action': 'Min',
        'name': 'EarliestJoinDate',
        'props': {}
    }, {
        'field': 'JoinDate',
        'action': 'Max',
        'name': 'LatestJoinDate',
        'props': {}
    }],
).execute(fileinput_152)

summarise_85 = Summarise(
    fields = [{
        'field': 'JoinDate',
        'action': 'Min',
        'name': 'EarliestJoinDate',
        'props': {}
    }, {
        'field': 'JoinDate',
        'action': 'Max',
        'name': 'LatestJoinDate',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

summarise_102 = Summarise(
    fields = [{
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Sum',
        'name': 'Sum_Spend',
        'props': {}
    }],
).execute(fileinput_152)

summarise_102 = Summarise(
    fields = [{
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }, {
        'field': 'Spend',
        'action': 'Sum',
        'name': 'Sum_Spend',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10009

# MISSING TOOL - Tool: DbFileOutput, id: 10009

# MISSING TOOL - Tool: BrowseV2, id: 10028

# MISSING TOOL - Tool: BrowseV2, id: 10028

summarise_115 = Summarise(
    fields = [{
        'field': 'FirstName',
        'action': 'Longest',
        'name': 'Longest_FirstName',
        'props': {}
    }, {
        'field': 'FirstName',
        'action': 'Shortest',
        'name': 'Shortest_FirstName',
        'props': {}
    }, {
        'field': 'LastName',
        'action': 'CountNonBlank',
        'name': 'CountNonBlank_LastName',
        'props': {}
    }, {
        'field': 'LastName',
        'action': 'CountBlank',
        'name': 'CountBlank_LastName',
        'props': {}
    }],
).execute(fileinput_152)

summarise_115 = Summarise(
    fields = [{
        'field': 'FirstName',
        'action': 'Longest',
        'name': 'Longest_FirstName',
        'props': {}
    }, {
        'field': 'FirstName',
        'action': 'Shortest',
        'name': 'Shortest_FirstName',
        'props': {}
    }, {
        'field': 'LastName',
        'action': 'CountNonBlank',
        'name': 'CountNonBlank_LastName',
        'props': {}
    }, {
        'field': 'LastName',
        'action': 'CountBlank',
        'name': 'CountBlank_LastName',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10015

# MISSING TOOL - Tool: DbFileOutput, id: 10015

summarise_95 = Summarise(
    fields = [{
        'field': 'State',
        'action': 'GroupBy',
        'name': 'State',
        'props': {}
    }, {
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }, {
        'field': 'SpatialObj',
        'action': 'SpatialObjCombine',
        'name': 'SpatialObjCombine_SpatialObj',
        'props': {}
    }, {
        'field': 'SpatialObj',
        'action': 'SpatialObjConvexHull',
        'name': 'SpatialObjConvexHull_SpatialObj',
        'props': {}
    }],
).execute(fileinput_152)

summarise_95 = Summarise(
    fields = [{
        'field': 'State',
        'action': 'GroupBy',
        'name': 'State',
        'props': {}
    }, {
        'field': 'City',
        'action': 'GroupBy',
        'name': 'City',
        'props': {}
    }, {
        'field': 'SpatialObj',
        'action': 'SpatialObjCombine',
        'name': 'SpatialObjCombine_SpatialObj',
        'props': {}
    }, {
        'field': 'SpatialObj',
        'action': 'SpatialObjConvexHull',
        'name': 'SpatialObjConvexHull_SpatialObj',
        'props': {}
    }],
).execute(fileinput_152)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007
