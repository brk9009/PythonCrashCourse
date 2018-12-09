#10.10 Python Crash Course
def count_the(filename):
    """Count the number of times 'the' appears."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        num = contents.lower().count('the')
        print(str(num))

count_the('moby_dick.txt')
