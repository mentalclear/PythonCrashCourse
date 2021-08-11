class Restaurant:
    """ A simple class for a restaurant """


    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} specializes in {self.cousine_type}.")


    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open today")


restaurant = Restaurant("Sea Beauty", "seafood")
print(restaurant.restaurant_name)
print(restaurant.cousine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
