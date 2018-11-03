#7.5 Python Crash Course
prompt = "What is your age? "

active = True
while active:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("\nYou get in for free.")
        active = False
    elif age >= 3 and age <= 12:
        print("\nIt'll cost 10 dollars.")
        active = False
    else:
        print("\nIt'll cost 15 dollars.")
        active = False
