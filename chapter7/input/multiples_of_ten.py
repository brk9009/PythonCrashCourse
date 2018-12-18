#7.3 Python Crash Course
number = input("Type in a number: ")
number = int(number)

if number % 10 == 0:
    print("\n" + str(number) + " is a multiple of 10.")
else:
    print("\n" + str(number) + " is not a multiple of 10.")
