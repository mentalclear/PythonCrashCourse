output_file = 'chapter10\exercises\programming_poll.txt'

def write_username_to_file(file):
    """ A function that asks a user why they like programming
        and puts their reply to a file
    """        
    print("Input 'quit' anytime to quit")
    while True:        
        username = input("What's your your name: ")
        if username != 'quit':
            reason = input("Why do you like programming? ")
            if reason != 'quit':
                with open(file, 'a') as file_obj:                
                    file_obj.write(f"{username} likes programming because: {reason}\n")
                    print(f"Thanks for you feedback {username}, we recorded your feedback")                
            else:
                "Exiting..."
                break
        else:
            break

                
write_username_to_file(output_file)
