#9.1 Python Crash Course
class Restaurant():
    """Create a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")

restaurant = Restaurant('Chipotle', 'Mexican')

print("The restaurant's name is " + restaurant.restaurant_name.title())
print("The cusine type is " + restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()
