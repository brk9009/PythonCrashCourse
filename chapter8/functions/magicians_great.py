#8.10 Python Crash Course
def make_great(magician_names):
    for magician_name in magician_names:
        magician_name = magician_name + " the Great"
        great_list.append(magician_name)

magician_names = ['David Blaine', 'Harry Houdini', 'Penn and Teller']
great_list = []

make_great(magician_names)
print(great_list)
