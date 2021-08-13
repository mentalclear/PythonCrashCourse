# Import multiple classes, explicitly
# from car import Car, ElectricCar

# Importing complete module
# import car 
# Now module name must be provided before creating and object
# my_beetle = car.Car('volkswagen','beetle', 2019)

# Importing all classes from a module
from car import *

my_beetle = Car('volkswagen','beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
