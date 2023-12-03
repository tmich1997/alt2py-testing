from tools import TextInput,Union,Join

textinput_82 = TextInput(
    columns = {
        'StreamNumber': ['1', '1', '1', '1'],
        'ID': ['1', '2', '3', '4'],
        'firstName': ['Tim', 'Isaac', 'Benjamin', 'Thomas'],
        'lastName': ['Berners-Lee', 'Newton', 'Franklin', 'Edison']
    },
).execute()

textinput_82 = TextInput(
    columns = {
        'StreamNumber': ['1', '1', '1', '1'],
        'ID': ['1', '2', '3', '4'],
        'firstName': ['Tim', 'Isaac', 'Benjamin', 'Thomas'],
        'lastName': ['Berners-Lee', 'Newton', 'Franklin', 'Edison']
    },
).execute()

textinput_89 = TextInput(
    columns = {
        'StreamNumber': ['2', '2', '2', '2'],
        'firstName': ['Louis', 'Alexander', 'Alfred', 'Henry'],
        'lastName': ['Pasteur', 'Bell', 'Nobel', 'Ford'],
        'ID': ['5', '6', '7', '8']
    },
).execute()

textinput_89 = TextInput(
    columns = {
        'StreamNumber': ['2', '2', '2', '2'],
        'firstName': ['Louis', 'Alexander', 'Alfred', 'Henry'],
        'lastName': ['Pasteur', 'Bell', 'Nobel', 'Ford'],
        'ID': ['5', '6', '7', '8']
    },
).execute()

union_86 = Union(
    subset = False,
).execute([textinput_82,textinput_89])

union_86 = Union(
    subset = False,
).execute([textinput_82,textinput_89])

# MISSING TOOL - Tool: DbFileOutput, id: 9999

# MISSING TOOL - Tool: DbFileOutput, id: 9999

textinput_98 = TextInput(
    columns = {
        'Field1': ['3', '3', '3', '3'],
        'Field2': ['9', '10', '11', '12'],
        'Field3': ['Louis', 'Edward', 'Charles', 'Edward'],
        'Field4': ['Braille', 'Teller', 'Goodyear', 'Jenner']
    },
).execute()

textinput_98 = TextInput(
    columns = {
        'Field1': ['3', '3', '3', '3'],
        'Field2': ['9', '10', '11', '12'],
        'Field3': ['Louis', 'Edward', 'Charles', 'Edward'],
        'Field4': ['Braille', 'Teller', 'Goodyear', 'Jenner']
    },
).execute()

union_101 = Union(
    subset = False,
).execute([textinput_82,textinput_98])

union_101 = Union(
    subset = False,
).execute([textinput_82,textinput_98])

# MISSING TOOL - Tool: DbFileOutput, id: 10007

# MISSING TOOL - Tool: DbFileOutput, id: 10007

textinput_104 = TextInput(
    columns = {
        'Field1': ['Zamboni', 'Harington', 'Paul', 'Reard'],
        'Field2': ['Frank', 'John', 'Les', 'Louis'],
        'Field3': ['4', '4', '4', '4'],
        'Field4': ['21', '22', '23', '24']
    },
).execute()

textinput_104 = TextInput(
    columns = {
        'Field1': ['Zamboni', 'Harington', 'Paul', 'Reard'],
        'Field2': ['Frank', 'John', 'Les', 'Louis'],
        'Field3': ['4', '4', '4', '4'],
        'Field4': ['21', '22', '23', '24']
    },
).execute()

union_105 = Union(
    subset = False,
    manual = [
        ['StreamNumber', 'ID', 'firstName', 'lastName'],
        ['Field3', 'Field4', 'Field2', 'Field1']
    ],
).execute([textinput_82,textinput_104])

union_105 = Union(
    subset = False,
    manual = [
        ['StreamNumber', 'ID', 'firstName', 'lastName'],
        ['Field3', 'Field4', 'Field2', 'Field1']
    ],
).execute([textinput_82,textinput_104])

# MISSING TOOL - Tool: DbFileOutput, id: 10001

# MISSING TOOL - Tool: DbFileOutput, id: 10001

textinput_106 = TextInput(
    columns = {
        'StreamNumber': ['5', '5', '5', '5'],
        'ID': ['25', '26', '27', '28'],
        'firstName': ['John', 'Orville', 'Wilbur', 'Dorothy'],
        'lastName': ['Deere', 'Wright', 'Wright', 'Gerber'],
        'Gender': ['M', 'M', 'M', 'F']
    },
).execute()

textinput_106 = TextInput(
    columns = {
        'StreamNumber': ['5', '5', '5', '5'],
        'ID': ['25', '26', '27', '28'],
        'firstName': ['John', 'Orville', 'Wilbur', 'Dorothy'],
        'lastName': ['Deere', 'Wright', 'Wright', 'Gerber'],
        'Gender': ['M', 'M', 'M', 'F']
    },
).execute()

union_107 = Union(
    subset = False,
).execute([textinput_82,textinput_106])

union_107 = Union(
    subset = False,
).execute([textinput_82,textinput_106])

# MISSING TOOL - Tool: DbFileOutput, id: 10003

# MISSING TOOL - Tool: DbFileOutput, id: 10003

union_109 = Union(
    order = ['#5', '#1'],
).execute([textinput_82,textinput_106])

union_109 = Union(
    order = ['#5', '#1'],
).execute([textinput_82,textinput_106])

# MISSING TOOL - Tool: DbFileOutput, id: 10005

# MISSING TOOL - Tool: DbFileOutput, id: 10005

textinput_144 = TextInput(
    columns = {
        'ID': ['1', '2'],
        'DataStream': ['X', 'X'],
        'Note': ['Join puts 2 streams next to each other.', 'Union puts 2+ streams on top of each other.']
    },
).execute()

textinput_144 = TextInput(
    columns = {
        'ID': ['1', '2'],
        'DataStream': ['X', 'X'],
        'Note': ['Join puts 2 streams next to each other.', 'Union puts 2+ streams on top of each other.']
    },
).execute()

textinput_145 = TextInput(
    columns = {
        'ID': ['1', '2'],
        'DataStream': ['Y', 'Y'],
        'Note': ['Join puts 2 streams next to each other.', 'Union puts 2+ streams on top of each other.']
    },
).execute()

textinput_145 = TextInput(
    columns = {
        'ID': ['1', '2'],
        'DataStream': ['Y', 'Y'],
        'Note': ['Join puts 2 streams next to each other.', 'Union puts 2+ streams on top of each other.']
    },
).execute()

union_146 = Union(
    subset = False,
).execute([textinput_144,textinput_145])

union_146 = Union(
    subset = False,
).execute([textinput_144,textinput_145])

join_148 = Join(
    left_keys = ['ID'],
    right_keys = ['ID'],
).execute(textinput_144,textinput_145)

join_148 = Join(
    left_keys = ['ID'],
    right_keys = ['ID'],
).execute(textinput_144,textinput_145)
