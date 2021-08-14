file_path = 'C:\AllLearning\AllPython\PythonCrashCourse\project\chapter10\pi_digits.txt'

# reading line by line
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip()) # Also stripping empty spces with rstrip()