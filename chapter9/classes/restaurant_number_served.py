#9.4 Python Crash Course
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

restaurant = Restaurant('Chipotle', 'Mexican')
restaurant.set_number_served(5)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)
