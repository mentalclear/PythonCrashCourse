user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# Fav languages sample too
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
print("\n")
for name in favorite_languages:  # same as favorite_languages.keys()
    print(name.title())

print("\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print("\n")

# Printing it out sorted
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Printing values
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# This approach pulls all the values from the dictionary without checking
# for repeats.

# to exclude duplications:
print("\nExcluding duplications: ")
for language in set(favorite_languages.values()):
    print(language.title())
# Only unique items will be printed out
