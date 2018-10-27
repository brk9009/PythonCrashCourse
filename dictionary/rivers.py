#6.5 Python Crash Course
rivers = {'nile': 'egypt',
            'amazon': 'brazil',
            'yangtze': 'china',}

print("\nPart 1:")
for name, country in rivers.items():
    print("The " + name.title() + " runs through " + country.title())

print("\nPart 2:")
for name in set(rivers.keys()):
    print(name.title())

print("\nPart 3:")
for country in set(rivers.values()):
    print(country.title())
