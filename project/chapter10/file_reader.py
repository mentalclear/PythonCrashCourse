file_path = 'C:\AllLearning\AllPython\PythonCrashCourse\project\chapter10\pi_digits.txt'

# reading the whole file
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip()) # removing empty string rstrip()