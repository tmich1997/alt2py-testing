from tools import TextInput,Transpose,Sort

textinput_123 = TextInput(
    columns = {
        'Product': ['Graphing Calculators', 'Office Supplies', 'Encyclopedias', 'Building Blocks', 'Books about Dinosaurs', 'Viggo Mortenson DVDs', 'Clothing', 'Frisbee and Frisbee Accessories', 'Legumes', 'Microscopes'],
        'Category': ['General', 'General', 'Educational', 'Fun and Games', 'Fun and Games', 'Fun and Games', 'General', 'Fun and Games', 'General', 'Educational'],
        'Suggested Age Range': ['13+', 'All ages', 'All ages', '3-6', 'All ages', '13+', 'All ages', '7+', 'All ages', '7+'],
        'Average Monthly Sales': ['84020.17', '83319.17', '79280.75', '97381.33', '106175.58', '117805.5', '121212.5', '92629.92', '116122.75', '602.83'],
        'January': ['191817', '156628', '6299', '8313', '193667', '181291', '6988', '4940', '73467', '206'],
        'February': ['434', '82183', '119153', '184270', '76441', '178860', '71830', '105607', '154459', '324'],
        'March': ['70654', '125043', '161717', '186021', '163244', '144830', '69881', '53949', '92995', '925'],
        'April': ['166571', '11205', '145195', '190255', '116158', '35341', '137635', '72655', '68466', '633'],
        'May': ['99066', '130896', '22305', '8211', '42346', '136331', '168495', '140850', '159429', '487'],
        'June': ['64423', '31214', '38385', '134736', '166919', '199431', '118806', '68332', '130945', '168'],
        'July': ['72846', '199932', '9183', '154287', '153584', '42309', '199716', '154956', '32288', '235'],
        'August': ['52744', '121453', '157398', '4735', '72374', '42458', '153901', '158538', '140673', '154'],
        'September': ['16150', '61049', '169316', '71620', '155810', '184727', '145946', '116732', '153088', '1432'],
        'October': ['98130', '16068', '30902', '113519', '44161', '80648', '20584', '153754', '73637', '861'],
        'November': ['42312', '18098', '74336', '20765', '55709', '54734', '190893', '46668', '176343', '530'],
        'December': ['133095', '46061', '17180', '91844', '33694', '132706', '169875', '34578', '137683', '1279']
    },
).execute()

textinput_123 = TextInput(
    columns = {
        'Product': ['Graphing Calculators', 'Office Supplies', 'Encyclopedias', 'Building Blocks', 'Books about Dinosaurs', 'Viggo Mortenson DVDs', 'Clothing', 'Frisbee and Frisbee Accessories', 'Legumes', 'Microscopes'],
        'Category': ['General', 'General', 'Educational', 'Fun and Games', 'Fun and Games', 'Fun and Games', 'General', 'Fun and Games', 'General', 'Educational'],
        'Suggested Age Range': ['13+', 'All ages', 'All ages', '3-6', 'All ages', '13+', 'All ages', '7+', 'All ages', '7+'],
        'Average Monthly Sales': ['84020.17', '83319.17', '79280.75', '97381.33', '106175.58', '117805.5', '121212.5', '92629.92', '116122.75', '602.83'],
        'January': ['191817', '156628', '6299', '8313', '193667', '181291', '6988', '4940', '73467', '206'],
        'February': ['434', '82183', '119153', '184270', '76441', '178860', '71830', '105607', '154459', '324'],
        'March': ['70654', '125043', '161717', '186021', '163244', '144830', '69881', '53949', '92995', '925'],
        'April': ['166571', '11205', '145195', '190255', '116158', '35341', '137635', '72655', '68466', '633'],
        'May': ['99066', '130896', '22305', '8211', '42346', '136331', '168495', '140850', '159429', '487'],
        'June': ['64423', '31214', '38385', '134736', '166919', '199431', '118806', '68332', '130945', '168'],
        'July': ['72846', '199932', '9183', '154287', '153584', '42309', '199716', '154956', '32288', '235'],
        'August': ['52744', '121453', '157398', '4735', '72374', '42458', '153901', '158538', '140673', '154'],
        'September': ['16150', '61049', '169316', '71620', '155810', '184727', '145946', '116732', '153088', '1432'],
        'October': ['98130', '16068', '30902', '113519', '44161', '80648', '20584', '153754', '73637', '861'],
        'November': ['42312', '18098', '74336', '20765', '55709', '54734', '190893', '46668', '176343', '530'],
        'December': ['133095', '46061', '17180', '91844', '33694', '132706', '169875', '34578', '137683', '1279']
    },
).execute()

transpose_133 = Transpose(
    key_fields = ['Product', 'Category', 'Suggested Age Range', 'Average Monthly Sales'],
    data_fields = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    sort = True,
).execute(textinput_123)

transpose_133 = Transpose(
    key_fields = ['Product', 'Category', 'Suggested Age Range', 'Average Monthly Sales'],
    data_fields = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    sort = True,
).execute(textinput_123)

sort_10004 = Sort(
    fields = ['Product', 'Category', 'Suggested Age Range', 'Average Monthly Sales'],
    orders = [True, True, True, True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(transpose_133)

sort_10004 = Sort(
    fields = ['Product', 'Category', 'Suggested Age Range', 'Average Monthly Sales'],
    orders = [True, True, True, True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(transpose_133)

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

transpose_134 = Transpose(
    key_fields = ['Product'],
    data_fields = ['Category', 'Suggested Age Range', 'Average Monthly Sales'],
    sort = True,
).execute(textinput_123)

transpose_134 = Transpose(
    key_fields = ['Product'],
    data_fields = ['Category', 'Suggested Age Range', 'Average Monthly Sales'],
    sort = True,
).execute(textinput_123)

sort_10005 = Sort(
    fields = ['Product'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(transpose_134)

sort_10005 = Sort(
    fields = ['Product'],
    orders = [True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(transpose_134)

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

transpose_135 = Transpose(
    key_fields = ['Product', 'Category', 'Suggested Age Range'],
    data_fields = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    sort = True,
).execute(textinput_123)

transpose_135 = Transpose(
    key_fields = ['Product', 'Category', 'Suggested Age Range'],
    data_fields = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    sort = True,
).execute(textinput_123)

sort_10006 = Sort(
    fields = ['Product', 'Category', 'Suggested Age Range'],
    orders = [True, True, True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(transpose_135)

sort_10006 = Sort(
    fields = ['Product', 'Category', 'Suggested Age Range'],
    orders = [True, True, True],
    handle_alpha_numeric = True,
    maintain_order = True,
).execute(transpose_135)

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003
