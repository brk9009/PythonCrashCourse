#10.4 Python Crash Course
"""Prompts users for name, greets them, then writes the names in guest_book.py"""

name_polling = True
filename = "guest_book.txt"

while name_polling:
    # Prompt user for name
    name = input("Enter your name (Enter 'q' to quit) ")

    if name != 'q':
        print("Welcome, " + name.title())

        with open(filename, 'a') as file_object:
            file_object.write(name.title() + " was there\n")
    else:
        name_polling = False
