def main():
    # write to a file and create if it's not available
    # f = open("textfile.txt", "w+")

    # append mode.
    # f = open("textfile.txt", "a")

    f = open("textfile.txt", "r")

    # for i in range(10):
    #     f.write("This is line " + str(i) + "\n")

    #f.close()

    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)

        # reading all content
        #contents = f.read()
        #print(contents)



if __name__ == '__main__':
    main()
