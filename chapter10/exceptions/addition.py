#10.6 Python Crash Course
print("Give me two numbers, and I'll add them.")

try:
    first_number = input("\nFirst number: ")
    first_number = int(first_number)

    second_number = input("Second number: ")
    second_number = int(second_number)

except ValueError:
    print("I need a number.")

else:
    answer = first_number + second_number
    print(str(answer))
