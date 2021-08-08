prompt = "\nPlease enter a series of pizza toppings you want"
prompt += "\nenter 'quit' when you are done"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("We’ll add " + topping.title() + " topping to your pizza")