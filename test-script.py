states = ['QLD', 'NSW']

# states = ['QLD', 'NSW', 'SA', 'ACT', 'TAS', 'NT', 'WA', 'VIC']



scales = ['Single', 'Couple']

# scales = ['Single', 'Couple', 'Family', 'SingleParentFamily', 'ExtendedFamily']



excesses = ['250', '500', '750']



for excess, state, scale in zip(excesses, states, scales):

    if 'excess' in json_data['variables']:

        json_data['variables']['excess'] = excess

    if 'state' in json_data['variables']:

        json_data['variables']['state'] = state

    if 'scale' in json_data['variables']:

        json_data['variables']['scale'] = scale
