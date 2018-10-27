#6.6 Python Crash Course
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['ben', 'andrew', 'jen', 'mike', 'phil']

for name in friends:
    if name in favorite_languages.keys():
        print("Thank you " + name.title() + ", for responding!")
    else:
        print(name.title() + ", you should take the poll!")
