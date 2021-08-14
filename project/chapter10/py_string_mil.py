file_path = 'C:\AllLearning\AllPython\PythonCrashCourse\project\chapter10\pi_million_digits.txt'

# reading line by line
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))