#10.7 Python Crash Course
print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit")

while True:
    try:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        first_number = int(first_number)

        second_number = input("Second number: ")
        if second_number == 'q':
            break
        second_number = int(second_number)

    except ValueError:
        print("I need a number.")

    else:
        answer = first_number + second_number
        print(str(answer))
