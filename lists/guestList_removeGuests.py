#3.6 Python Crash Course (no loops)
guest_list = ['Terrell Davis', 'Michael Jordan', 'Scottie Pippen', 'John Elway', 'Gary Sanchez', 'Luis Severino']
message = "I can only invite two of " + guest_list[0].title() + ", " + guest_list[1].title() + ", " + guest_list[2].title() + ", " + guest_list[3].title() + ", " + guest_list[4].title() + ", and " + guest_list[5].title()
print(message)

removed_guest = guest_list.pop(0)
print("Sorry " + removed_guest.title() + ", you can't go with us")

removed_guest = guest_list.pop(4)
print("Sorry " + removed_guest.title() + ", you can't go with us")

removed_guest = guest_list.pop(3)
print("Sorry " + removed_guest.title() + ", you can't go with us")

removed_guest = guest_list.pop(1)
print("Sorry " + removed_guest.title() + ", you can't go with us")

message = "Hey " + guest_list[0].title() + " and " +  guest_list[1].title() + ", you can still come with."
print(message)

del guest_list[0]
del guest_list[0]
print(guest_list)
