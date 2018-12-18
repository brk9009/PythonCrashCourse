#9.5 Python Crash Course
class User():
    """Creates a user"""

    def __init__(self, first_name, last_name, username, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("First name: " + self.first_name.title() + " Last name: " + self.last_name.title() +
            " Username: " + self.username.title() + " Location: " + self.location.title())

    def greet_user(self):
        print("Welcome, " + self.username.title())

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0

new_user = User('ben', 'kixmiller', 'brk', 'walnut')
new_user.increment_login_attempts()
print(new_user.login_attempts)

new_user.reset_login_attempts()
print(new_user.login_attempts)
