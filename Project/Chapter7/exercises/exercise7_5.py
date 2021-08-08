prompt = "\nBefore purchasing a ticket please input your age: "
prompt += "\nenter 0 to quit"

while True:
    age = int(input(prompt))

    if age == 0:
        break
    elif 0 < age <= 3:
        print("Your ticket cost is: Free")
    elif 3 < age <= 12:
        print("Your ticket cost is: $10")
    else:
        print("Your ticket cost is: $15")
