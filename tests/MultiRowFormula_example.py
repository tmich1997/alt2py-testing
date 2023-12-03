from tools import TextInput,MultiRowFormula,CrossTab

textinput_121 = TextInput(
    columns = {
        'DeviceID': ['2', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '4', '4', '4'],
        'Clicks': ['2015-11-30 03:17:04', '2015-12-06 17:22:00', '2015-12-06 17:22:02', '2016-01-30 06:34:19', '2016-01-30 06:34:25', '2016-01-30 06:34:32', '2016-02-10 23:59:50', '2016-02-11 00:00:16', '2015-10-18 03:17:04', '2015-11-06 17:22:00', '2015-11-06 17:22:02', '2016-12-30 06:34:19', '2016-12-30 06:34:25', '2016-12-30 06:34:32', '2016-12-31 23:59:50', '2017-01-01 00:00:16']
    },
).execute()

textinput_121 = TextInput(
    columns = {
        'DeviceID': ['2', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '4', '4', '4'],
        'Clicks': ['2015-11-30 03:17:04', '2015-12-06 17:22:00', '2015-12-06 17:22:02', '2016-01-30 06:34:19', '2016-01-30 06:34:25', '2016-01-30 06:34:32', '2016-02-10 23:59:50', '2016-02-11 00:00:16', '2015-10-18 03:17:04', '2015-11-06 17:22:00', '2015-11-06 17:22:02', '2016-12-30 06:34:19', '2016-12-30 06:34:25', '2016-12-30 06:34:32', '2016-12-31 23:59:50', '2017-01-01 00:00:16']
    },
).execute()

multirowformula_120 = MultiRowFormula(
    field = "Flag",
    groupings = ['DeviceID'],
    num_rows = 1,
    expression = "IF DateTimeDiff([Clicks],[Row-1:Clicks],'seconds')<30
    THEN 1
    ELSE 0
    ENDIF ",
    size = "1",
    unknown = "empty",
).execute(textinput_121)

multirowformula_120 = MultiRowFormula(
    field = "Flag",
    groupings = ['DeviceID'],
    num_rows = 1,
    expression = "IF DateTimeDiff([Clicks],[Row-1:Clicks],'seconds')<30
    THEN 1
    ELSE 0
    ENDIF ",
    size = "1",
    unknown = "empty",
).execute(textinput_121)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

textinput_123 = TextInput(
    columns = {
        'DownloadData': ['<post>', '<article>', 'Behind the Scenes of the Tool Mastery Series: Community APIs and Automation', '</article>', '<attributes>', '<views>', '170', '</views>', '<stars>', '6', '</stars>', '<comments>', '1', '</comments>', '</attributes>', '</post>', '<post>', '<article>', 'How the Join Tool Works and Why You Might Be Getting More Records than Expected', '</article>', '<attributes>', '<views>', '387', '</views>', '<stars>', '6', '</stars>', '<comments>', '1', '</comments>', '</attributes>', '</post>', '<post>', '<article>', 'Convert a Workflow into an App', '</article>', '<attributes>', '<views>', '109', '</views>', '<stars>', '6', '</stars>', '<comments>', '2', '</comments>', '</attributes>', '</post>']
    },
).execute()

textinput_123 = TextInput(
    columns = {
        'DownloadData': ['<post>', '<article>', 'Behind the Scenes of the Tool Mastery Series: Community APIs and Automation', '</article>', '<attributes>', '<views>', '170', '</views>', '<stars>', '6', '</stars>', '<comments>', '1', '</comments>', '</attributes>', '</post>', '<post>', '<article>', 'How the Join Tool Works and Why You Might Be Getting More Records than Expected', '</article>', '<attributes>', '<views>', '387', '</views>', '<stars>', '6', '</stars>', '<comments>', '1', '</comments>', '</attributes>', '</post>', '<post>', '<article>', 'Convert a Workflow into an App', '</article>', '<attributes>', '<views>', '109', '</views>', '<stars>', '6', '</stars>', '<comments>', '2', '</comments>', '</attributes>', '</post>']
    },
).execute()

multirowformula_122 = MultiRowFormula(
    field = "Headers",
    num_rows = 1,
    expression = "IF !StartsWith([DownloadData], '<')
    THEN trim([Row - 1: DownloadData], '<>')
    ELSE null()
    ENDIF ",
    size = "254",
    unknown = "empty",
).execute(textinput_123)

multirowformula_122 = MultiRowFormula(
    field = "Headers",
    num_rows = 1,
    expression = "IF !StartsWith([DownloadData], '<')
    THEN trim([Row - 1: DownloadData], '<>')
    ELSE null()
    ENDIF ",
    size = "254",
    unknown = "empty",
).execute(textinput_123)

multirowformula_124 = MultiRowFormula(
    field = "post",
    num_rows = 1,
    expression = 'IF [DownloadData]="<post>"
    THEN[Row - 1: post] + 1
    ELSE[Row - 1: post]
    ENDIF ',
    size = "254",
    unknown = "empty",
).execute(multirowformula_122)

multirowformula_124 = MultiRowFormula(
    field = "post",
    num_rows = 1,
    expression = 'IF [DownloadData]="<post>"
    THEN[Row - 1: post] + 1
    ELSE[Row - 1: post]
    ENDIF ',
    size = "254",
    unknown = "empty",
).execute(multirowformula_122)

crosstab_125 = CrossTab(
    groupings = ['post'],
    header = "Headers",
    value_field = "DownloadData",
    method = "First",
    sep = ",",
).execute(multirowformula_124)

crosstab_125 = CrossTab(
    groupings = ['post'],
    header = "Headers",
    value_field = "DownloadData",
    method = "First",
    sep = ",",
).execute(multirowformula_124)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005

textinput_115 = TextInput(
    columns = {
        'Year': ['2012', None, None, None, None, None, None, None, None, None, None, None, '2013', None, None, None, None, None, None, None, None, None, None, None, '2014', None, None, None, None, None, '2012', None, None, None, None, None, None, None, None, None, None, None, '2013', None, None, None, None, None, None, None, None, None, None, None, '2014', None, None, None, None, None, '2012', None, None, None, None, None, None, None, None, None, None, None, '2013', None, None, None, None, None, None, None, None, None, None, None, '2014', None, None, None, None, None],
        'Month': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6'],
        'Product': ['Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C'],
        'Sales': ['290', '398', '444', '368', '482', '428', '416', '420', '402', '400', '388', '394', '358', '406', '392', '474', '490', '464', '368', '482', '460', '396', '470', '484', '406', '376', '404', '568', '205', '634', '1675606', '2207660', '2444242', '1986294', '2287008', '2288512', '2307460', '2054136', '2103286', '2161064', '2206844', '2260564', '2064074', '2293626', '2169230', '2468444', '2566232', '2350834', '2025940', '2592014', '2389344', '2205798', '2722910', '2723290', '2507608', '2154678', '2413078', '2973512', '1118660', '3069538', '42', '110', '106', '62', '74', '72', '98', '76', '52', '62', '92', '104', '76', '112', '82', '100', '104', '86', '92', '94', '96', '76', '92', '100', '110', '94', '86', '104', '92', '118']
    },
).execute()

textinput_115 = TextInput(
    columns = {
        'Year': ['2012', None, None, None, None, None, None, None, None, None, None, None, '2013', None, None, None, None, None, None, None, None, None, None, None, '2014', None, None, None, None, None, '2012', None, None, None, None, None, None, None, None, None, None, None, '2013', None, None, None, None, None, None, None, None, None, None, None, '2014', None, None, None, None, None, '2012', None, None, None, None, None, None, None, None, None, None, None, '2013', None, None, None, None, None, None, None, None, None, None, None, '2014', None, None, None, None, None],
        'Month': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6'],
        'Product': ['Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_A', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_B', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C', 'Prod_C'],
        'Sales': ['290', '398', '444', '368', '482', '428', '416', '420', '402', '400', '388', '394', '358', '406', '392', '474', '490', '464', '368', '482', '460', '396', '470', '484', '406', '376', '404', '568', '205', '634', '1675606', '2207660', '2444242', '1986294', '2287008', '2288512', '2307460', '2054136', '2103286', '2161064', '2206844', '2260564', '2064074', '2293626', '2169230', '2468444', '2566232', '2350834', '2025940', '2592014', '2389344', '2205798', '2722910', '2723290', '2507608', '2154678', '2413078', '2973512', '1118660', '3069538', '42', '110', '106', '62', '74', '72', '98', '76', '52', '62', '92', '104', '76', '112', '82', '100', '104', '86', '92', '94', '96', '76', '92', '100', '110', '94', '86', '104', '92', '118']
    },
).execute()

multirowformula_116 = MultiRowFormula(
    field = "Year",
    num_rows = 1,
    expression = "IF IsNull([Year])
    THEN[Row - 1: Year]
    ELSE[Year]
    ENDIF ",
    size = None,
).execute(textinput_115)

multirowformula_116 = MultiRowFormula(
    field = "Year",
    num_rows = 1,
    expression = "IF IsNull([Year])
    THEN[Row - 1: Year]
    ELSE[Year]
    ENDIF ",
    size = None,
).execute(textinput_115)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

multirowformula_118 = MultiRowFormula(
    field = "3 Month Average",
    groupings = ['Product'],
    num_rows = 2,
    expression = "Average([Sales],[Row-1:Sales],[Row-2:Sales])",
    size = "12.2",
    unknown = "nearest",
).execute(textinput_115)

multirowformula_118 = MultiRowFormula(
    field = "3 Month Average",
    groupings = ['Product'],
    num_rows = 2,
    expression = "Average([Sales],[Row-1:Sales],[Row-2:Sales])",
    size = "12.2",
    unknown = "nearest",
).execute(textinput_115)

# MISSING TOOL - Tool: DbFileOutput, id: 10009

# MISSING TOOL - Tool: DbFileOutput, id: 10009

multirowformula_117 = MultiRowFormula(
    field = "RecordID",
    groupings = ['Product'],
    num_rows = 1,
    expression = "[Row-1:RecordID]+1",
    size = "254",
    unknown = "empty",
).execute(textinput_115)

multirowformula_117 = MultiRowFormula(
    field = "RecordID",
    groupings = ['Product'],
    num_rows = 1,
    expression = "[Row-1:RecordID]+1",
    size = "254",
    unknown = "empty",
).execute(textinput_115)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001
