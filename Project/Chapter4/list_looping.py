magicians = ['alice', 'david', 'carolina']
# simple loop
for magician in magicians:
    print(magician)

# More additions to loops
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thanks everybody that was a great show!")