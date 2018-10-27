favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("\nExercise 1:")
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
            language.title() + ".")

print("\nExercise 2:")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

print("\nExercise 3:")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\nExercise 4:")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\nExercise 5:")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
