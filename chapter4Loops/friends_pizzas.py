#4.11 Python Crash Course
pizzas = ['cheese', 'pepperoni', 'sausage']
friend_pizzas = pizzas[:]

pizzas.append('hamburger')
friend_pizzas.append('supreme')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
