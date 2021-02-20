#
# Just a comment
#


def main():
    x, y = 10, 100

    # Conditionals
    if (x < y):
        st = "x less than y"
    elif (x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"

    print(st)

    # conditional statements
    st = "x is less than y" if (x < y) else "x is greater than or the same as y"
    print(st)


if __name__ == '__main__':
    main()
