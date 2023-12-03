from tools import TextInput,Clean

textinput_123 = TextInput(
    columns = {
        'CustomerID': ['49', '456', '31', '5', '1', '2', None],
        'FirstName': ['Thomas', 'Galileo  ', 'Benjamin', 'Dorothy', 'Louis', 'Tim', None],
        'LastName': ['Edison', None, 'Franklin', 'Gerber', ' Pasteur', 'Berners-Lee', None],
        'Term': ['12 months', '12 months', '36 months', '12 months', '60 months', '36 months', None],
        'JoinDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2014-10-01', '2013-09-06', '2014-01-26', None],
        'Region': ['South', 'South', 'Midwest', 'Northeast', 'West', ' Midwest', None],
        'Score': ['2', None, '1', '22', '4', '5', None],
        'FirstPurchaseDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2012-05-05', '2013-09-06', '2014-01-26', None],
        'Empty': [None, None, None, None, None, None, None]
    },
).execute()

textinput_123 = TextInput(
    columns = {
        'CustomerID': ['49', '456', '31', '5', '1', '2', None],
        'FirstName': ['Thomas', 'Galileo  ', 'Benjamin', 'Dorothy', 'Louis', 'Tim', None],
        'LastName': ['Edison', None, 'Franklin', 'Gerber', ' Pasteur', 'Berners-Lee', None],
        'Term': ['12 months', '12 months', '36 months', '12 months', '60 months', '36 months', None],
        'JoinDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2014-10-01', '2013-09-06', '2014-01-26', None],
        'Region': ['South', 'South', 'Midwest', 'Northeast', 'West', ' Midwest', None],
        'Score': ['2', None, '1', '22', '4', '5', None],
        'FirstPurchaseDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2012-05-05', '2013-09-06', '2014-01-26', None],
        'Empty': [None, None, None, None, None, None, None]
    },
).execute()

clean_126 = Clean(
    fields = ['Score'],
    replace_na_zero = True,
    modify = None,
    remove_punctuation = False,
    modifier = None,
).execute(textinput_123)

clean_126 = Clean(
    fields = ['Score'],
    replace_na_zero = True,
    modify = None,
    remove_punctuation = False,
    modifier = None,
).execute(textinput_123)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

clean_127 = Clean(
    fields = ['CustomerID', 'FirstName', 'LastName', 'JoinDate', 'Region', 'Score', 'FirstPurchaseDate'],
    replace_na_blank = True,
    trim_whitespace = True,
    modify = None,
    remove_punctuation = False,
    modifier = None,
).execute(textinput_123)

clean_127 = Clean(
    fields = ['CustomerID', 'FirstName', 'LastName', 'JoinDate', 'Region', 'Score', 'FirstPurchaseDate'],
    replace_na_blank = True,
    trim_whitespace = True,
    modify = None,
    remove_punctuation = False,
    modifier = None,
).execute(textinput_123)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

clean_128 = Clean(
    fields = ['Term'],
    replace_na_blank = True,
    replace_na_zero = True,
    trim_whitespace = True,
    remove_letters = True,
    modify = None,
    remove_punctuation = False,
    modifier = None,
).execute(textinput_123)

clean_128 = Clean(
    fields = ['Term'],
    replace_na_blank = True,
    replace_na_zero = True,
    trim_whitespace = True,
    remove_letters = True,
    modify = None,
    remove_punctuation = False,
    modifier = None,
).execute(textinput_123)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

clean_129 = Clean(
    fields = ['Region'],
    trim_whitespace = True,
    modify = None,
    remove_punctuation = False,
    modifier = "upper",
).execute(textinput_123)

clean_129 = Clean(
    fields = ['Region'],
    trim_whitespace = True,
    modify = None,
    remove_punctuation = False,
    modifier = "upper",
).execute(textinput_123)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005

clean_132 = Clean(
    filter_na_cols = True,
    filter_na_rows = True,
    modify = None,
    remove_punctuation = False,
    modifier = None,
).execute(textinput_123)

clean_132 = Clean(
    filter_na_cols = True,
    filter_na_rows = True,
    modify = None,
    remove_punctuation = False,
    modifier = None,
).execute(textinput_123)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007
