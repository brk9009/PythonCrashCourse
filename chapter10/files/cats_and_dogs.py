#10.8 and 10.9 Python Crash Course

cats_filename = "cats.txt"
dogs_filename = "dogs.txt"

try:
    with open(cats_filename) as cats_object:
        cats_contents = cats_object.read()

    with open(dogs_filename) as dogs_object:
        dog_contents = dogs_object.read()

except FileNotFoundError:
    pass

else:
    print(cats_contents)
    print(dog_contents.strip())
