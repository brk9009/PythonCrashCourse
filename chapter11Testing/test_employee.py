import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):
    """Test functions in 'employee.py'"""

    def setUp(self):
        """Create an employee"""
        self.employee = Employee('Ben', 'Kixmiller', 40000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 45000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 50000)

unittest.main()
