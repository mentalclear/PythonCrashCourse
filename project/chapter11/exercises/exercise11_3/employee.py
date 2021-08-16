class Employee:
    """ This is an Employee simulation accepts:
        First name, Last name and base salary 
    """

    def __init__(self, first_name, last_name, salary):
        """ Initilizing an emplyee with all values """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, the_raise=5000):
        """ Each year emplyee gets a raise """
        self.salary += the_raise

