#9.3 Python Crash Course
class User():
    """Creates a user"""

    def __init__(self, first_name, last_name, username, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.location = location

    def describe_user(self):
        print("First name: " + self.first_name.title() + " Last name: " + self.last_name.title() +
            " Username: " + self.username.title() + " Location: " + self.location.title())

    def greet_user(self):
        print("Welcome, " + self.username.title())

user1 = User('ben', 'kixmiller', 'gostate', 'Des Moines')
user1.describe_user()
user1.greet_user()

user2 = User('jeremy', 'both', 'jeremyboth', 'Omaha')
user2.describe_user()
user2.greet_user()
