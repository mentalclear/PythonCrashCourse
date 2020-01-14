from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = datetime.now()
    print(today)

    t = datetime.time(datetime.now())
    print(t)

    # today = date.today()
    # print("today is",  today)
    #
    # # individual day objects
    # print("Date components: ", today.day, today.month, today.year)
    #
    # # weekday numbers
    # print("todays weekday ", today.weekday())
    # days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    # print ("Whis is a: ", days[today.weekday()])




if __name__ == '__main__':
    main()