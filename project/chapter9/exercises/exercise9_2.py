class Restaurant:
    """ A simple class for a restaurant """


    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} specializes in {self.cousine_type}.")


    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open today")

restaurant1 = Restaurant("Highland Views", "contemporary")
restaurant2 = Restaurant("Taco Place", "mexican")
restaurant3 = Restaurant("Peruvian Taste", "peruvian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
