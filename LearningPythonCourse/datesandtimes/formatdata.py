from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime("This year is %Y"))
    print(now.strftime("%a, %d %B, %y"))

    print(now.strftime("Locale date/time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))


if __name__ == '__main__':
    main()