from tools import TextInput,Sort

textinput_64 = TextInput(
    columns = {
        'CustomerID': ['49', '456', '31', '5', '1', '2', None],
        'FirstName': ['Thomas', 'Galileo', 'Benjamin', 'Dorothy', 'Louis', 'Tim', None],
        'LastName': ['Edison', None, 'Franklin', 'Franklin', 'Pasteur', 'Berners-Lee', None],
        'Gender': ['M', 'M', 'M', 'F', 'M', 'M', None],
        'JoinDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2014-10-01', '2013-09-06', '2014-01-26', None],
        'Region': ['South', 'South', 'Midwest', 'Northeast', 'West', 'Midwest', None],
        'Score': ['2e', 'a1d', 'a1c', '22b', '4a', 'a', None]
    },
).execute()

textinput_64 = TextInput(
    columns = {
        'CustomerID': ['49', '456', '31', '5', '1', '2', None],
        'FirstName': ['Thomas', 'Galileo', 'Benjamin', 'Dorothy', 'Louis', 'Tim', None],
        'LastName': ['Edison', None, 'Franklin', 'Franklin', 'Pasteur', 'Berners-Lee', None],
        'Gender': ['M', 'M', 'M', 'F', 'M', 'M', None],
        'JoinDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2014-10-01', '2013-09-06', '2014-01-26', None],
        'Region': ['South', 'South', 'Midwest', 'Northeast', 'West', 'Midwest', None],
        'Score': ['2e', 'a1d', 'a1c', '22b', '4a', 'a', None]
    },
).execute()

sort_26 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    maintain_order = True,
).execute(textinput_64)

sort_26 = Sort(
    fields = ['CustomerID'],
    orders = [True],
    maintain_order = True,
).execute(textinput_64)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

sort_37 = Sort(
    fields = ['LastName', 'FirstName'],
    orders = [True, True],
    maintain_order = True,
).execute(textinput_64)

sort_37 = Sort(
    fields = ['LastName', 'FirstName'],
    orders = [True, True],
    maintain_order = True,
).execute(textinput_64)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

sort_11 = Sort(
    fields = ['Score'],
    orders = [True],
    maintain_order = True,
).execute(textinput_64)

sort_11 = Sort(
    fields = ['Score'],
    orders = [True],
    maintain_order = True,
).execute(textinput_64)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

sort_42 = Sort(
    fields = ['Score'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(textinput_64)

sort_42 = Sort(
    fields = ['Score'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(textinput_64)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005
