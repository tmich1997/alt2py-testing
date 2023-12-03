from tools import TextInput,DateTime,Select

textinput_137 = TextInput(
    columns = {
        'Customer ID': ['1', '2', '3', '4', '5', '6'],
        'Join Date': ['2005-01-10', '2015-03-14', '2009-10-13', '2010-09-30', '2014-12-31', '2016-11-05'],
        'DOB': ['January 24, 1977', 'July 06, 1952', 'October 12, 1988', 'February 29, 1984', 'June 19, 1979', 'May 12, 1965'],
        'Last save date': ['09-15/2015', '09-11/2015', '09-13/2015', None, '08-22/2015', '12-04/2016'],
        'Last login datetime': ['2015-09-15 12:25:31', '2015-09-12 03:42:06', '2015-09-13 19:20:58', None, '2015-08-22 10:00:00', '2016-12-05 11:52:45'],
        'Last login time': ['12:25:31', '03:42:06', '19:20:58', None, '10:00:00', '11:52:45']
    },
).execute()

textinput_137 = TextInput(
    columns = {
        'Customer ID': ['1', '2', '3', '4', '5', '6'],
        'Join Date': ['2005-01-10', '2015-03-14', '2009-10-13', '2010-09-30', '2014-12-31', '2016-11-05'],
        'DOB': ['January 24, 1977', 'July 06, 1952', 'October 12, 1988', 'February 29, 1984', 'June 19, 1979', 'May 12, 1965'],
        'Last save date': ['09-15/2015', '09-11/2015', '09-13/2015', None, '08-22/2015', '12-04/2016'],
        'Last login datetime': ['2015-09-15 12:25:31', '2015-09-12 03:42:06', '2015-09-13 19:20:58', None, '2015-08-22 10:00:00', '2016-12-05 11:52:45'],
        'Last login time': ['12:25:31', '03:42:06', '19:20:58', None, '10:00:00', '11:52:45']
    },
).execute()

datetime_136 = DateTime(
    field = "DOB",
    to_string = False,
    pattern = "Month dd, yyyy",
    label = "DOB_New",
).execute(textinput_137)

datetime_136 = DateTime(
    field = "DOB",
    to_string = False,
    pattern = "Month dd, yyyy",
    label = "DOB_New",
).execute(textinput_137)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

datetime_135 = DateTime(
    field = "Join Date",
    pattern = "Month dd, yyyy",
    label = "Join Date_New",
).execute(textinput_137)

datetime_135 = DateTime(
    field = "Join Date",
    pattern = "Month dd, yyyy",
    label = "Join Date_New",
).execute(textinput_137)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

datetime_140 = DateTime(
    field = "Last login datetime",
    pattern = "day, dd Month, yyyy",
    label = "Last login date",
).execute(textinput_137)

datetime_140 = DateTime(
    field = "Last login datetime",
    pattern = "day, dd Month, yyyy",
    label = "Last login date",
).execute(textinput_137)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

datetime_159 = DateTime(
    field = "Join Date",
    pattern = "day, Month dd, yyyy",
    label = "Join Date_New",
).execute(textinput_137)

datetime_159 = DateTime(
    field = "Join Date",
    pattern = "day, Month dd, yyyy",
    label = "Join Date_New",
).execute(textinput_137)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007

datetime_163 = DateTime(
    field = "Last save date",
    to_string = False,
    pattern = "MM-dd/yyyy",
    label = "Last save date_New",
).execute(textinput_137)

datetime_163 = DateTime(
    field = "Last save date",
    to_string = False,
    pattern = "MM-dd/yyyy",
    label = "Last save date_New",
).execute(textinput_137)

# MISSING TOOL - Tool: DbFileOutput, id: 10009

# MISSING TOOL - Tool: DbFileOutput, id: 10009

select_171 = Select(
    selected = ['Last login time'],
    keep_unknown = True,
    reorder = False,
    change_types = {
        'Last login time': 'String'
    },
).execute(textinput_137)

select_171 = Select(
    selected = ['Last login time'],
    keep_unknown = True,
    reorder = False,
    change_types = {
        'Last login time': 'String'
    },
).execute(textinput_137)

datetime_143 = DateTime(
    field = "Last login time",
    to_string = False,
    pattern = "HH:mm:ss",
    label = "Last login time_new",
).execute(select_171)

datetime_143 = DateTime(
    field = "Last login time",
    to_string = False,
    pattern = "HH:mm:ss",
    label = "Last login time_new",
).execute(select_171)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005
