from user import User
from privileges import Privileges

class Admin(User):
    """ A class that represents an Admin user """

    def __init__(self, first_name, last_name, username, email, location):
        """Initilizing the Admin"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()