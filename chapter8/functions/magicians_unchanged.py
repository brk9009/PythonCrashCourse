#8.11 Python Crash Course
def show_magicians(magician_names):
    print("\nRegular names:")
    for magician_name in magician_names:
        print(magician_name)

def make_great(magician_names):
    print("\nGreat names:")
    for magician_name in magician_names:
        magician_name = magician_name + " the Great"
        great_list.append(magician_name)

magician_names = ['David Blaine', 'Harry Houdini', 'Penn and Teller']
great_list = []

make_great(magician_names[:])
print(great_list)

show_magicians(magician_names)
show_magicians(great_list)
