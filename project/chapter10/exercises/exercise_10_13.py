import json


def get_stored_username():
    """ Get strored username if available """
    filename = "chapter10\\exercises\\username.json"

    try:
        with open(filename) as f:            
            try:
                username = json.load(f)
            except json.decoder.JSONDecodeError:
                get_new_username() 
                username = json.load(f)         
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'chapter10\\exercises\\username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """ Greet user name by name """    
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")        


greet_user()        