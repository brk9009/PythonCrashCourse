#5.9 Python Crash Course
current_users = ['john', 'ben', 'mike', 'jake', 'tyler']
new_users = ['kelvin', 'mark', 'chris', 'markos', 'tyler']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("You will need to enter a new user name, " + user.title())
    else:
        print(new_user.title() + " is available.")
