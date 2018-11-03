#3.6 Python Crash Course (no loops)
guest_list = ['Michael Jordan', 'John Elway', 'Gary Sanchez']
message = "Hey " + guest_list[0].title() + ", " + guest_list[1].title() + ", and " + guest_list[2].title() + ", we've found a bigger table."
print(message)

guest_list.insert(0, 'Terrell Davis')
print(guest_list)

guest_list.insert(2, 'Scottie Pippen')
print(guest_list)

guest_list.append('Luis Severino')
print(guest_list)

message = "Hey " + guest_list[0].title() + ", want to go grab some food?"
print(message)

message = "Hey " + guest_list[1].title() + ", want to go grab some food?"
print(message)

message = "Hey " + guest_list[2].title() + ", want to go grab some food?"
print(message)

message = "Hey " + guest_list[3].title() + ", want to go grab some food?"
print(message)

message = "Hey " + guest_list[4].title() + ", want to go grab some food?"
print(message)

message = "Hey " + guest_list[5].title() + ", want to go grab some food?"
print(message)
