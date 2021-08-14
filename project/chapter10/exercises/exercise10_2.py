file_path = 'chapter10\exercises\learning_python.txt'

def read_line_by_line(file):
    """ Reading contents of a file by looping through"""
    with open(file) as file_object:
        for line in file_object:            
            print(line.rstrip().replace('Python', 'C'))

print("Printing changed results with C insteda of Python:")
read_line_by_line(file_path)