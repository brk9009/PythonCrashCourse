#5.2 Python Crash Course
state = 'Iowa'
print("Is the state Iowa?")
print(state == 'Iowa')

print("Is the state not Nebraska?")
print(state == 'Nebraska')

name = 'Ben'
print("Is my name with lower method, ben?")
print(name.lower() == 'ben')

print("Is my name with lower method, Ben?")
print(name.lower() == 'Ben')

fav_number = 23
print("Is my favorite number, 23?")
print(fav_number == 23)

print("Is my favorite number 5?")
print(fav_number == 5)

print("Is my favorite number over 20?")
print(fav_number > 20)

print("Is my favorite number less than 22?")
print(fav_number < 22)

print("Is my favorite number between 10 and 25?")
print(fav_number >= 10 and fav_number <= 25)

print("Is my favorite number 20 or 25?")
print(fav_number == 20 or fav_number == 25)

friends = ['mike', 'josh', 'andrew', 'jeremy']
friend = 'andrew'

if friend in friends:
    print(friend.lower() + ' is in the list.')

friend = 'cody'
if friend not in friends:
    print(friend.lower() + ' is not in the list.')
