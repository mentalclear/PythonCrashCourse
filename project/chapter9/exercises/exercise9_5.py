class User:
    """ A user modeling class """

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0


    def describe_user(self):
        """ Display user's summary """
        print(f"{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")        
        print(f"E-mail: {self.email}")
        print(f"Location: {self.location}")


    def greet_user(self):
        print(f"\nHowdy, {self.username} welcome back!")


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0



tester = User("Tedd", "Tess", "teddtess", "teddtess@example.com", "Austin, TX")
tester.describe_user()
tester.greet_user()

print("\nMaking 3 logggin attempts")
tester.increment_login_attempts()
tester.increment_login_attempts()
tester.increment_login_attempts()
print(f"User {tester.username} attempted to login {tester.login_attempts} times")

print("\nResetting login attempts...")
tester.reset_login_attempts()
print(f"User {tester.first_name}, login attempts: {tester.login_attempts}")