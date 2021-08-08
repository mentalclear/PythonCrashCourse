def dream_vacation_poll():
    responses = {}

    while True:
        name = input("\nWhat is your name? ")
        response = input("If you could visit one place in the world, where would you go? ")

        # Store the response in the dictionary:
        if name in responses:
            print("You have already voted!")
        else:
            responses[name] = response

        # Find out if anyone else is going to take the poll.
        repeat = input("Would you like to let another person respond? (yes/ no) ")
        if repeat == 'no':
            break

    print("\n*** Poll Results ***")
    for name, response in responses.items():
        print(name + " would like to go to " + response + ".")


dream_vacation_poll()
