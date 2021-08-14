file_path = 'C:\AllLearning\AllPython\PythonCrashCourse\project\chapter10\pi_digits.txt'

# reading line by line
with open(file_path) as file_object:
    list = file_object.readlines();    

print(list)