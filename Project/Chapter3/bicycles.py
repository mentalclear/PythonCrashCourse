bicycles = ['GT', 'trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# one item from the list
print(bicycles[0])
print(bicycles[0].title())  # Capitalized first letter

# Important thing -1 is the last item in the list
print(bicycles[-1])  # And this way it continues from the back

print(bicycles[-3])  # cannondale

message = "My first good bicycle was " + bicycles[0] + "."
print(message)
