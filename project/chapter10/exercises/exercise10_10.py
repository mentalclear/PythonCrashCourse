def count_words(filename, word):
    """Count how many times word appears in the text."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents=f.read()
    except(FileNotFoundError):
        print(f"The {filename} was not found")       
    else:        
        word_times = contents.lower().count(word)
        print(f"\nThe file {filename} contains '{word}' about {word_times} times\n")


filenames = ['chapter10\exercises\\adventures_of_sherlock_holmes.txt', 
'chapter10\exercises\\the_hound_of_baskervilles.txt']

word = "sherlock"

for filename in filenames:
    count_words(filename, word)