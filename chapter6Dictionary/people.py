#6.7 Python Crash Course
person_0 = {'first_name': 'ben',
            'last_name': 'kixmiller',
            'age': 26,
            'city': 'walnut'}

person_1 = {'first_name': 'jeremy',
            'last_name': 'bothwell',
            'age': 26,
            'city': 'omaha'}

person_2 = {'first_name': 'andrew',
            'last_name': 'finnell',
            'age': 25,
            'city': 'walnut'}

people = [person_0, person_1, person_2]

for person in people:
    full_name = "Full name: " + person['first_name'].title() + " " + person['last_name'].title()
    print("\n" + full_name)
    print("Age: " + str(person['age']))
    print("Location: " + person['city'])
