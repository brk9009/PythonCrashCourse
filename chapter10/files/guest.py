#10.3 Python Crash Course
"""Enter your name and write to guest.txt."""
name = input("Enter your name: ")

filename = "guest.txt"

with open(filename, 'w') as file_object:
    file_object.write(name)
