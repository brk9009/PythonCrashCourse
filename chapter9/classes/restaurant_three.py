#9.2 Python Crash Course
class Restaurant():
    """Create a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")

restaurant1 = Restaurant('Chipotle', 'Mexican')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('Fazolis', 'Italian')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Popeyes', 'American')
restaurant3.describe_restaurant()
