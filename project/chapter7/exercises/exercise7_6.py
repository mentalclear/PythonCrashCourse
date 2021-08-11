prompt = "\nPlease enter a series of pizza toppings you want"
prompt += "\nEnter 'quit' when you are done"


def using_quit():
    while True:
        topping = input(prompt)
        if topping == 'quit':
            break
        else:
            print("We’ll add " + topping.title() + " topping to your pizza")


def using_flag():
    active = True
    while active:
        topping = input(prompt)
        if topping == 'quit':
            active = False
        else:
            print("We’ll add " + topping.title() + " topping to your pizza")


def using_conditional():
    index = 1
    while index <= 3:
        topping = input(prompt + " Maximum 3 toppings allowed")
        if topping == 'quit':
            break
        else:
            index += 1
            print("We’ll add " + topping.title() + " topping to your pizza")


using_conditional()
