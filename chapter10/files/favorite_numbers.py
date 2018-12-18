#10.11 Python Crash Course
import json

def get_new_favorite_number():
    filename = 'favorite_number.json'
    favorite_number = input("What's your favorite number?")

    with open(filename, 'w') as file_obj:
        json.dump(favorite_number, file_obj)

def get_stored_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as file_obj:
            favorite_number = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_favorite_number():
    favorite_number = get_stored_favorite_number()
    if favorite_number:
        print("I know your favorite number! It's " + favorite_number)
    else:
        favorite_number = get_new_favorite_number()
        print("Your new favorite number is " + favorite_number)

get_favorite_number()
