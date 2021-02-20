import os
from os import *
import datetime
from datetime import date, time, timedelta
import time

def main():
   print(os.name)
   print("Item exists: " + str(path.exists("textfile.txt")))
   print("is it a file: " + str(path.isfile("textfile.txt")))
   print("is it a dir: " + str(path.isdir("textfile.txt")))

   # local path
   print("Real path: " + str(path.realpath("textfile.txt")))
   print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

   # files modeif time
   t = time.ctime(path.getmtime("textfile.txt"))
   print(t)

   print(datetime.datetime.fromtimestamp((path.getmtime("textfile.txt"))))

   td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
       path.getmtime("textfile.txt")
   )
   print ("it sbeen " + str(td) + " since last modification")
   print("or, " + str(td.total_seconds()) + " seconds")


if __name__ == '__main__':
    main()