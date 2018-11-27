#10.5 Python Crash Course
"""Asks why you like programming, stores responses in programming_poll.txt"""

polling_Active = True
filename = "programming_poll.txt"

while polling_Active:
    response = input("Why do you like programming? (Press 'q' to quit) ")

    if response != 'q':
        with open(filename, 'a') as file_object:
            file_object.write(response + "\n")
    else:
        polling_Active = False
