favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll_people = {'jason', 'alex', 'george', 'sarah', 'phil'}
for person in sorted(poll_people):
    if person in favorite_languages.keys():
        print(person.title() + " thanks for participating in the poll!")
    else:
        print(person.title() + " please participate in the poll!")
