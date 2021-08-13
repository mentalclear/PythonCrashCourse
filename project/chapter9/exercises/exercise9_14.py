from random import randint
from random import choice

class Lottery():
    """ A class that represents a Lottery"""

    def __init__(self, list_of_items):
        self.list_of_items = list_of_items


    def play_lottery_ticket(self):
         """ This method randomly selects items from the list """
         lucky_ticket = []
         for item in range(4):
            selection = choice(self.list_of_items)
            #selection = self.list_of_items[randint(1, len(self.list_of_items)-1)] 
            print (f"We pulled a {selection}!")
            lucky_ticket.append(selection)    
         return lucky_ticket

list_items = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D')

lottery = Lottery(list_items)
print(f"The final winning ticket is:  {lottery.play_lottery_ticket()}")