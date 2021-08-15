def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents=f.read()
    except(FileNotFoundError):
        print(f"The {filename} was not found")
        # pass  # Silently pass the exception
    else:
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")


# filename = 'chapter10\\alice.txt'
# count_words(filename)

filenames = ['chapter10\\alice.txt', 'siddhartha.txt', 'chapter10\\moby_dick.txt', 'chapter10\\little_women.txt']

for filename in filenames:
    count_words(filename)