class Restaurant:
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


restaurant = Restaurant("Sea Beauty", "seafood")
print(restaurant.restaurant_name)
print(restaurant.cousine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"The restaurant served {restaurant.number_served} customers")

restaurant.set_number_served(1)
print(f"The restaurant served {restaurant.number_served} customers")

restaurant.increment_number_served(-10)
restaurant.increment_number_served(5)
print(f"The restaurant served {restaurant.number_served} customers")
