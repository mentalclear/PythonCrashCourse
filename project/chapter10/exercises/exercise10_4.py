output_file = 'chapter10\exercises\guest_book.txt'

def write_username_to_file(file):
    """ A function that asks a user for their name
        greets them and puts their name into a guestbook
    """    
    print("Input 'quit' when you are done")
    while True:        
        username = input("What's your name: ")
        if username != 'quit':
            with open(file, 'a') as file_obj:                
                file_obj.write(f"{username} visited today\n")
                print(f"Greetings {username}, glad you stopped by today!")
                print("Your name was added to our guestbook")                
        else:
            "Exiting..."
            break

                
write_username_to_file(output_file)
