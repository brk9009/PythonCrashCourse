#9.13 Python Crash Course
from collections import OrderedDict

glossary = OrderedDict()

glossary['loop'] = 'a way to go through a list with very little code.'
glossary['list'] = 'a data structure to hold an array of elements.'
glossary['if-else'] = 'a way to decide between two or more choices.'
glossary['tuples'] = 'a list that can/t be modifed.'
glossary['dictionary'] = 'storing a key-value pair to an object similar to hash maps'
glossary['.title()'] = 'capitalize each word in a string.'
glossary['.str()'] = 'represent non-string variables as strings.'
glossary['.sort()'] = 'sort by alphabetical order.'
glossary['.set()'] = 'returns a list of unique items. (No duplicates)'

for key, value in glossary.items():
    print("\nWord: " + key.title())
    print("Definition: " + value.title())
