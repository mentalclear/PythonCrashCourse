file_path = 'chapter10\exercises\learning_python.txt'

def read_whole(file):
    """ Reads the content of a file as a whole"""
    with open(file) as file_object:
        content = file_object.read()
    print(content.rstrip())


def read_line_by_line(file):
    """ Reading contents of a file by looping through"""
    with open(file) as file_object:
        for line in file_object:
            print(line.rstrip())


def read_list_of_lines(file):
    """ Creating a list of lines from a file """    
    with open(file) as file_object:
        line_list = file_object.readlines()
        for line in line_list:
            print(line.rstrip())


print("Printing contents as a whole: ")
read_whole(file_path)

print("Printing contents by looping through lines: ")
read_line_by_line(file_path)

print("Printing contents by creating a list of lines: ")
read_list_of_lines(file_path)
