#9.6 Python Crash Course
class Restaurant():
    """Create a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant."""
        print("Restaurant name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        """Prints that the restaurant is open"""
        print(self.restaurant_name.title() + " is open")

    def set_number_served(self, customers):
        """Sets the number of people served."""
        self.number_served = customers

    def increment_number_served(self, customers):
        """Add the customers to the number of people served."""
        self.number_served += customers

class IceCreamStand(Restaurant):
    """Create an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla','chocolate','strawberry']

    def display_flavors(self):
        print("\nIce Cream Flavors served here: ")
        for flavor in self.flavors:
            print(flavor.title())

iceCreamStand = IceCreamStand('Cold Stone Creamery', 'Ice Cream')
iceCreamStand.display_flavors()
