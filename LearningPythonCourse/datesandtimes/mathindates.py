from datetime import *


def main():
    print(timedelta(days=365, hours=5, minutes=1))

    now = datetime.now()
    print("today is: " + str(now))

    # one year from now
    print("One year form now it'll be: " + str(now + timedelta(days=365)))


if __name__ == '__main__':
    main()