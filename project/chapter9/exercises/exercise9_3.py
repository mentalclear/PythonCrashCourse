class User:
    """ A user modeling class """

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location


    def describe_user(self):
        print(f"User {self.first_name} {self.last_name} is from"
                f"{self.location} and is {self.age} years old.")    


    def greet_user(self):
        print(f"Howdy {self.first_name} {self.last_name} how are you today?")


dimm = User("Dmitrii", "Kilishek", 43, "Sterling, VA")
tester = User("Tedd", "Tess", 33, "Austin, TX")

dimm.describe_user()
dimm.greet_user()
print("\n")
tester.describe_user()
tester.greet_user()
