#6.10 Python Crash Course
favorite_numbers = {'Ben': [23],
                    'Mike': [8,4],
                    'Andrew': [35,2],
                    'Jeremy': [15,2],
                    'Tyler': [28],
    }

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are ")

    for number in numbers:
        print(" " + str(number))
