import json

def favorite_number():
    input_file = 'chapter10\exercises\\favorite_number.json'
    try:
        with open(input_file) as f:
            number = json.load(f)            
    except FileNotFoundError:
        number = input("What's your favorite number? ")
        with open(input_file, 'w') as f:
            json.dump(number, f)
        print("Thanks, I'll remember that.")
    else:
        print(f"I know your favorite number! It's {number}")

favorite_number()

