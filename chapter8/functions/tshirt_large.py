#8.4 Python Crash Course
def make_shirt(message='I love Python', size='large'):
    """Gets the size and message on the shirt"""
    print("\nThe size of the t-shirt is " + str(size) + " and the message is " + message)

make_shirt(size='medium')
make_shirt()
make_shirt('Go Ben', 'medium')
