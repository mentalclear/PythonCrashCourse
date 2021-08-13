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
            