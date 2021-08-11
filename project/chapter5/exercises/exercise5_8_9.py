# Hello Admin
usernames = ['tester1', 'user1', 'tester2', 'admin', 'user2']
# usernames = []

if usernames:
    for name in usernames:
        if name == 'admin':
            print("Hello " + name + ", would you like to see a status report?")
        else:
            print("Hello " + name.title() + ", thank you for logging in again")
else:
    print("The list is empty!")