from random import randint

class Die():
    """ A class that represents a Die"""

    def __init__(self, sides=6):
        self.sides = sides


    def roll_die(self):
        """ This method rolls the die using random"""
        return randint(1, self.sides)


die = Die()
results = []
for roll_number in range(10):
    result = die.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)
        