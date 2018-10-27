#6.3 and 6.4 Python Crash Course
glossary = {'loop': 'a way to go through a list with very little code.',
            'list': 'a data structure to hold an array of elements.',
            'if-else': 'a way to decide between two or more choices.',
            'tuples': 'a list that can/t be modifed.',
            'dictionary': 'storing a key-value pair to an object similar to hash maps',
            '.title()': 'capitalize each word in a string.',
            '.str()': 'represent non-string variables as strings.',
            '.sort()': 'sort by alphabetical order.',
            '.set()': 'returns a list of unique items. (No duplicates)'}

for key, value in glossary.items():
    print("\nWord: " + key.title())
    print("Definition: " + value.title())
