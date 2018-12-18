#7.4 Python Crash Course
prompt = "Type a pizza topping you want on your pizza."
prompt += "\nType 'quit' to stop adding toppings. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print("I'll add " + message + " to your pizza.")
