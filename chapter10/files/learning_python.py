#10.1 Python Crash Course
filename = "learning_python.txt"

with open(filename) as file_object:
    print("\nRun 1")
    contents = file_object.read()
    print(contents.strip())

with open(filename) as file_object:
    print("\nRun 2")
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()

print("\nRun 3")
for line in lines:
    print(line.strip())
