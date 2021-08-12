class Restaurant():
    """ A simple class for a restaurant """


    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = 0

    
    def describe_restaurant(self):
        """ Prints formatted restaruant description"""
        print(f"The restaurant {self.restaurant_name} specializes in {self.cousine_type}.")


    def open_restaurant(self):
        """ Prints that restaurant is opened """
        print(f"The restaurant {self.restaurant_name} is open today")


    def set_number_served(self, amount):
        """ Sets the number of served customers """
        if amount >= self.number_served:
            self.number_served = amount
        else:
            print("Number of served customers cannot be decreased")

    
    def increment_number_served(self, number):
        if (self.number_served + number) >= self.number_served:
            self.number_served += number
        else:
            print("You cannot decrement the amount of served customers")

class IceCreamStand(Restaurant):
    """ Represent Icecream stand """


    def __init__(self, name, cousine_type='ice_cream'):
        super().__init__(name, cousine_type)
        self.flavors = []

    
    def display_flavors(self):
        print("Our icecream stand offres these flavors: ")
        for flavor in self.flavors:
            print(f" - {flavor.title()}") 


the_stand = IceCreamStand('Cold Stone Creamery')
the_stand.flavors = ['vanilla', 'chocolate', 'see salt caramel', 'buttered pecan', 'strawberry']

the_stand.describe_restaurant()
the_stand.display_flavors()
