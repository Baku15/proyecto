rivers  =   {
    'nile': 'egypt',
    'mississippi':   'united states',
    'fraser':    'canada',
    'kuskokwin':    'alaska',
    'yangtze':    'china',
}

for key, val1 in rivers.items():
    print(f"The {key.title()} runs through {val1.title()}")

for key1 in rivers.keys():
    print(f"\n the name are: {key1.title()}")

for val2 in rivers.values():
    #country = rivers[val2]
    print(f"\n the country: {val2.title()}")
