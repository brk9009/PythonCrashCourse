vacations = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    vacation = input("What is your dream vacation? ")

    vacations[name] = vacation

    repeat = input("Would you like another person to respond? (yes/ no)")
    if repeat == 'no':
        active = False

print("\n -- Poll results --")
for name, vacation in vacations.items():
    print(name.title() + " would like to go to " + vacation.title())
