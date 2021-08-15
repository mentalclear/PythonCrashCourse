import json

def store_favorite_number():
    number = input("What's your favorite number? ")
    output_file = 'chapter10\exercises\\favorite_number.txt'
    try:
        with open(output_file, 'w') as f:
            json.dump(number, f)
            print("Thanks! I'll remember that one")
    except FileNotFoundError:
        print(f"Couldn't store the response in a file {output_file}")

def get_favorite_number():
    input_file = 'chapter10\exercises\\favorite_number.txt'
    try:
        with open(input_file) as f:
            number = json.load(f)
            print(f"I know your favorite number! It’s {number}")
    except FileNotFoundError:        
        print(f"Couldn't read a file {input_file}")
    

store_favorite_number()
get_favorite_number()
