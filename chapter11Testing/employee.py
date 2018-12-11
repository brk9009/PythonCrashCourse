#11.3 Python Crash Course

class Employee():
    """Employee that gets a default or custom raise"""

    def __init__(self, first_name, last_name, salary):
        """Stores first name, last name, and salary"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amount=''):
        if raise_amount:
            self.salary += raise_amount
        else:
            self.salary += 5000
