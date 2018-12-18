#6.2 and #6.12 Python Crash Course
favorite_numbers = {'Ben': 23,
                    'Mike': 8,
                    'Andrew': 35,
                    'Jeremy': 15,
                    'Tyler':28}

# Before loops for dictionaries
print("\nBefore learning loops")
print("Ben's favorite number is: " + str(favorite_numbers['Ben']))
print("Mike's favorite number is: " + str(favorite_numbers['Mike']))
print("Andrew's favorite number is: " + str(favorite_numbers['Andrew']))
print("Jeremy's favorite number is: " + str(favorite_numbers['Jeremy']))
print("Tyler's favorite number is: " + str(favorite_numbers['Tyler']))

# After loops
print("\nAfter learning looping:")
for name, number in favorite_numbers.items():
    print(name.title() + "'s favorite number is: " + str(number))
