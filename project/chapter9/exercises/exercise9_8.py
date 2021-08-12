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
        print(f"  Username: {self.username}")        
        print(f"  E-mail: {self.email}")
        print(f"  Location: {self.location}")


    def greet_user(self):
        print(f"\nHowdy, {self.username} welcome back!")


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    """ Privileges specific class"""

    def __init__(self, privileges=[]):
        """ Initializing the class """
        self.privileges = privileges


    def show_privileges(self):
        """ Printing Admin privileges """        
        print("User Admin holds following privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(" - This user has no privileges")

class Admin(User):
    """ A class that represents an Admin user """

    def __init__(self, first_name, last_name, username, email, location):
        """Initilizing the Admin"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()
    

superadmin = Admin('james','bond', 'agent007', 'jbond@spys.org', 'guess')
superadmin.describe_user()

superadmin.privileges.show_privileges()

print("\nAdding privileges...")
superadmin_privileges = ["can add post", "can delete post", "can edit post", "can ban user", "can create user"]

superadmin.privileges.privileges = superadmin_privileges
superadmin.privileges.show_privileges()
