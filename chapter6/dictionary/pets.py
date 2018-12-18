#6.8 Python Crash Course
leah = {'name': 'leah',
        'animal': 'dog',
        'owner': 'ben',
        }

jake = {'name': 'jake',
        'animal': 'dog',
        'owner': 'ben',
        }

pets = [leah,jake]

for pet in pets:
    print("My pet's name is " + pet['name'].title() + ". Its a " + pet['animal'] +
        ". Its owner is " + pet['owner'].title() + ".")
