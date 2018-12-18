#3.10 Python Crash Course
languages = []
languages.append('english')
languages.append('spanish')
languages.append('german')
print(languages)
print("The last one in the list: " + languages[1])

languages.insert(1, 'chinese')
print(languages)

del languages[1]
print(languages)

languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)

languages.reverse()
print(languages)

print(len(languages))
