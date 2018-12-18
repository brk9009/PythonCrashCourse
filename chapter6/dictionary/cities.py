#6.11 Python Crash Course
cities = {
    'new york': {
        'country': 'usa',
        'population': 100000000,
        'fact': 'im a big yankees fan',
    },
    'walnut': {
        'country': 'usa',
        'population': 900,
        'fact': 'i went to school there',
    },
    'omaha': {
        'country': 'usa',
        'population': 100000,
        'fact': 'i go there to shop',
    },
}

for city_name, city_info in cities.items():
    print("The city's name: " + city_name.title())
    print("\tThe country that the city is in is the: " + city_info['country'].title())
    print("\tThe population is: " + str(city_info['population']))
    print("\tA cool fact about the city is: " + city_info['fact'])
