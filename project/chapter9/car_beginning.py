class Car:
    """ A simple car representation """

    def __init__(self, make, model, year):
        """Initializing attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Declaring a field and setting default value


    def get_descriptive_name(self):
        """ Return neatly formated descriptive name """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Printing the car milage info"""
        print(f"This car has {self.odometer_reading} miles on it")


    def update_odometer(self, milage):
        """
        Method to update the milage on a car to given value
        Rejecting the change if it attempts to roll the odometer back
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cannot roll back the odometer!")


    def increment_odomenter(self, miles):
        """ Add the given amount of miles to the odomenter reading""" 
        if (self.odometer_reading + miles) >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("You cannot decrement the odometer reading")

my_new_car = Car('mersedes-benz', 's500', 2021)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23  # Changing the value for a field directly
my_new_car.read_odometer()
print("\nAfter some driving... ")
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(1235)
my_new_car.read_odometer()
my_new_car.update_odometer(12)
my_new_car.update_odometer(1236)
my_new_car.read_odometer()

print("\nNow about the old car")
my_old_car = Car('subaru', 'outback', 2015)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometer(23_500)
my_old_car.read_odometer()

my_old_car.increment_odomenter(100)
my_old_car.read_odometer()

my_old_car.increment_odomenter(-100)
my_old_car.read_odometer()
