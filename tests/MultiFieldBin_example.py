from tools import TextInput,MultiFieldBin

textinput_8 = TextInput(
    columns = {
        'Employee': ['Elena Diaz', 'Jacob Miller', 'David Wright', 'Erin Lewis', 'Miranda Davis', 'Bellamy Anderson', 'Jennifer Kim', 'Shawn Jackson', 'Andrew Newsome', 'Wanda Sauer', "Aidan O'Rourke", 'Juan Hernandez', 'Laila Bryant', 'Watson Davies', 'Fiona Jones', 'Denise Myers', 'Patrick Tremont', 'Neville Pearson', 'Aditya Patel', 'Priscilla Hyler'],
        'Enterprise Sales 2015': ['898340', '8955', '48000', '18032', '89038', '874789', '78939', '550000', '0', '890000', '10500', '789999', '89034', '98900', '7900', '983498', '30400', '0', '53000', '102000'],
        'Commercial Sales 2015': ['8923', '108000', '96700', '78320', '89430', '5500', '22000', '0', '103000', '0', '76000', '3200', '113000', '13000', '200000', '0', '109000', '250000', '117000', '21700'],
        'Other Sales 2015': ['0', '98798', '98734', '78923', '80234', '0', '9033', '1266', '8000', '5400', '0', '45400', '4200', '80000', '7600', '5430', '6400', '4300', '9000', '40000'],
        'Number of Years in Current Position': ['5', '3', '8', '12', '4', '2', '1', '6', '7', '4', '9', '11', '10', '14', '2', '3', '1', '5', '6', '2'],
        '401k Contribution for 2015': ['10000', '20000', '18000', '12000', '15000', '13000', '9000', '11000', '14000', '14500', '13200', '12000', '11000', '16000', '17500', '13400', '15430', '17000', '16500', '17000']
    },
).execute()

textinput_8 = TextInput(
    columns = {
        'Employee': ['Elena Diaz', 'Jacob Miller', 'David Wright', 'Erin Lewis', 'Miranda Davis', 'Bellamy Anderson', 'Jennifer Kim', 'Shawn Jackson', 'Andrew Newsome', 'Wanda Sauer', "Aidan O'Rourke", 'Juan Hernandez', 'Laila Bryant', 'Watson Davies', 'Fiona Jones', 'Denise Myers', 'Patrick Tremont', 'Neville Pearson', 'Aditya Patel', 'Priscilla Hyler'],
        'Enterprise Sales 2015': ['898340', '8955', '48000', '18032', '89038', '874789', '78939', '550000', '0', '890000', '10500', '789999', '89034', '98900', '7900', '983498', '30400', '0', '53000', '102000'],
        'Commercial Sales 2015': ['8923', '108000', '96700', '78320', '89430', '5500', '22000', '0', '103000', '0', '76000', '3200', '113000', '13000', '200000', '0', '109000', '250000', '117000', '21700'],
        'Other Sales 2015': ['0', '98798', '98734', '78923', '80234', '0', '9033', '1266', '8000', '5400', '0', '45400', '4200', '80000', '7600', '5430', '6400', '4300', '9000', '40000'],
        'Number of Years in Current Position': ['5', '3', '8', '12', '4', '2', '1', '6', '7', '4', '9', '11', '10', '14', '2', '3', '1', '5', '6', '2'],
        '401k Contribution for 2015': ['10000', '20000', '18000', '12000', '15000', '13000', '9000', '11000', '14000', '14500', '13200', '12000', '11000', '16000', '17500', '13400', '15430', '17000', '16500', '17000']
    },
).execute()

multifieldbin_9 = MultiFieldBin(
    fields = ['Enterprise Sales 2015'],
    bins = 2,
).execute(textinput_8)

multifieldbin_9 = MultiFieldBin(
    fields = ['Enterprise Sales 2015'],
    bins = 2,
).execute(textinput_8)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

multifieldbin_10 = MultiFieldBin(
    fields = ['Enterprise Sales 2015'],
    mode = "interval",
    bins = 2,
).execute(textinput_8)

multifieldbin_10 = MultiFieldBin(
    fields = ['Enterprise Sales 2015'],
    mode = "interval",
    bins = 2,
).execute(textinput_8)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

multifieldbin_19 = MultiFieldBin(
    fields = ['Enterprise Sales 2015'],
    bins = 3,
).execute(textinput_8)

multifieldbin_19 = MultiFieldBin(
    fields = ['Enterprise Sales 2015'],
    bins = 3,
).execute(textinput_8)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

multifieldbin_21 = MultiFieldBin(
    fields = ['Enterprise Sales 2015', 'Commercial Sales 2015'],
    bins = 3,
).execute(textinput_8)

multifieldbin_21 = MultiFieldBin(
    fields = ['Enterprise Sales 2015', 'Commercial Sales 2015'],
    bins = 3,
).execute(textinput_8)

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005

multifieldbin_23 = MultiFieldBin(
    fields = ['Enterprise Sales 2015', 'Commercial Sales 2015'],
    mode = "interval",
    bins = 3,
).execute(textinput_8)

multifieldbin_23 = MultiFieldBin(
    fields = ['Enterprise Sales 2015', 'Commercial Sales 2015'],
    mode = "interval",
    bins = 3,
).execute(textinput_8)

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007
