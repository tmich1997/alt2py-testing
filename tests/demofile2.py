textinput_78 = TextInput(
    columns = {
        'CustomerID': ['1', '2', '5', '31', '49', '328', None],
        'FirstPurchaseDate': ['2013-09-06', '2014-01-26', '2012-05-05', '2014-12-21', '2014-08-21', '2014-08-22', None]
    },
).execute()

textinput_97 = TextInput(
    columns = {
        'ID': ['1', '2'],
        'DataStream': ['X', 'X'],
        'Note': ['Join puts 2 streams next to each other.', 'Union puts 2+ streams on top of each other.']
    },
).execute()

textinput_98 = TextInput(
    columns = {
        'ID': ['1', '2'],
        'DataStream': ['Y', 'Y'],
        'Note': ['Join puts 2 streams next to each other.', 'Union puts 2+ streams on top of each other.']
    },
).execute()

textinput_110 = TextInput(
    columns = {
        'CustomerID': ['49', '456', '31', '5', '1', '2', '3'],
        'FirstName': ['Thomas', 'Galileo', 'Benjamin', 'Dorothy', 'Louis', 'Tim', 'Timmy'],
        'LastName': ['Edison', None, 'Franklin', 'Gerber', 'Pasteur', 'Berners-Lee', 'Berners'],
        'Gender': ['M', 'M', 'M', 'F', 'M', 'M', 'F'],
        'JoinDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2014-10-01', '2013-09-06', '2014-01-26', '2014-01-25']
    },
).execute()

union_99 = Union(
    subset = False,
).execute([textinput_97,textinput_98])

join_79 = Join(
    left_keys = ['CustomerID'],
    right_keys = ['CustomerID'],
).execute(textinput_110,textinput_78)

join_101 = Join(
    left_keys = ['ID'],
    right_keys = ['ID'],
).execute(textinput_97,textinput_98)

textinput_111 = TextInput(
    columns = {
        'FirstName': ['Thomas', 'Galileo', 'Benjamin', 'Dorothy', 'Louis', 'Tim'],
        'LastName': ['Edison', None, 'Franklin', 'Gerber', 'Pasteur', 'Berners-Lee'],
        'FirstPurchaseDate': ['2014-08-21', '2014-04-01', '2014-12-21', '2012-05-05', '2013-09-06', '2014-01-26']
    },
).execute()

join_85 = Join(
    left_keys = ['FirstName', 'LastName'],
    right_keys = ['FirstName', 'LastName'],
).execute(textinput_110,textinput_111)

join_91 = Join(
    how = "position",
).execute(textinput_110,textinput_111)
