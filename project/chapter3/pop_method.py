motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#  The pop() method removes the last item in a list, but it lets you work
#  with that item after removing it

popped_motorcycle = motorcycles.pop()  # Pretty much removes the last element, changes the list!
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['kawasaki', 'honda', 'yamaha', 'suzuki']
print("\nList of motorcycles in the beginning:")
print(motorcycles)
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")
print("Now the motorcycles list after all: ")
print(motorcycles)
