output_file = 'chapter10\exercises\guest.txt'

def write_username_to_file(file):
    with open(file, 'a') as file_obj:
        username = input('Please input your name: ')
        file_obj.write(username)

write_username_to_file(output_file)

