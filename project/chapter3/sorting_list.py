cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# Permanently sorts the list
cars.sort()
print(cars)

# Reversing the sort
cars.sort(reverse=True)
print(cars)

# Restoring the original list
cars = ['bmw', 'audi', 'toyota', 'subaru']

# Temporary sorting the list
print("Here's the original list: ")
print(cars)
print("\nHere's the sorted list of cars:")
print(sorted(cars))
print("\nHere's the original list again: ")
print(cars)

# Printing the list in reverse order
print("\nPrinting the list in reverse order")
print(cars)
cars.reverse()
print(cars)

# Finding length of a list
print(len(cars))



