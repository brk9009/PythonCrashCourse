#7.9 Python Crash Course
sandwich_orders = ['pastrami','pastrami', 'ham and cheese', 'bacon ranch', 'pastrami', 'meatball']

print("The deli has ran out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
