#9.7 and 9.8 Python Crash Course
from user import User

class Privileges():
    """A class that has the privileges of admin accounts."""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """List the privileges of an admin."""
        print("Here is what an admin account can do: ")
        for privilege in self.privileges:
            print(privilege.title())

class Admin(User):
    """Creates an admin account."""

    def __init__(self, first_name, last_name, username, location):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an admin account.
        """
        super().__init__(first_name, last_name, username, location)
        self.privileges = Privileges(['can add post','can delete post','can ban user'])

#account = Admin('ben', 'kixmiller', 'brk', 'walnut')
#account.privileges.show_privileges()
