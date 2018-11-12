#8.16 Python Crash Course
import magicians_function
from magicians_function import show_magicians
from magicians_function import show_magicians as magicians
import magicians_function as mf
from magicians_function import *

magician_names = ['David Blaine', 'Harry Houdini', 'Penn and Teller']

print("\nAll functions:")
magicians_function.show_magicians(magician_names)

print("\nSpecific function:")
show_magicians(magician_names)

print("\nSpecific function (alias):")
magicians(magician_names)

print("\nModule (alias):")
mf.show_magicians(magician_names)

print("\nImport all functions (Don't use):")
show_magicians(magician_names)
