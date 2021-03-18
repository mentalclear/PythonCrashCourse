def print_life_stage(age):
    if age < 2:
        stage = "a baby"
    elif 2 <= age < 4:         # Example of simplified chained comparison
        stage = "a toddler"
    # elif age >= 4 and age < 13:  # 4 <= age < 13
    elif 4 <= age < 13:
        stage = "a kid"
    elif 13 <= age < 20:
        stage = "a teenager"
    elif 20 <= age < 65:
        stage = "an adult"
    elif age >= 65:
        stage = "an elder"
    else:
        stage = "nobody knows in what stage you are!"

    print("Your age is: " + str(age) + " and you are " + stage)


# Just to have some fun here:
for current_age in range(0, 101):
    print_life_stage(current_age)
