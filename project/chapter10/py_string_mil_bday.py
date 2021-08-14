file_path = 'C:\AllLearning\AllPython\PythonCrashCourse\project\chapter10\pi_million_digits.txt'

# reading line by line
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your bday, in a form of mmddyy: ")
if birthday in pi_string:
    print("Your bday appears in first million digits of pi!")
else:
    print("Your bday doesn't appear in first million digits of pi")
