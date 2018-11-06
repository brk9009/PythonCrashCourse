#7.8 Python Crash Course
sandwich_orders = ['ham and cheese', 'bacon ranch', 'meatball']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()

    print("I made your " + sandwich_order)
    finished_sandwiches.append(sandwich_order)

print(finished_sandwiches)
