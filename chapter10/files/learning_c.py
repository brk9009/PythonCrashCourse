#10.2 Python Crash Course
filename = "learning_python.txt"

with open(filename) as file_object:
    for line in file_object:
        line = line.strip()
        print(line.replace('Python','C'))
