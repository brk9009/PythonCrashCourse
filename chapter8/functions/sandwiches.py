#8.12 Python Crash Course
def make_sandwich(*toppings):
    """Make a sandwich using any number of toppings"""
    print("\nToppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich('bread', 'mayo', 'cheese')
make_sandwich('lettuce', 'ham')
make_sandwich('bread', 'peanut butter', 'jelly', 'butter')
