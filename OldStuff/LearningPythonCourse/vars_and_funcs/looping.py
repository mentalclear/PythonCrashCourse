def main():
    x = 0

    # While
    while x < 5:
        print(x)
        x = x + 1

    # For loop
    for x in range(5, 10):
        print(x)

    # For loop over a collection
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    # break and continue
    for x in range(10, 20):
        # if(x==14): break   <- break example
        if (x % 2 == 0): continue
        print(x)

    # Using enumerate func
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print(i, d)


if __name__ == '__main__':
    main()
