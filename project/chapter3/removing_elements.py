motorcycles = ['kawasaki', 'honda', 'yamaha', 'suzuki']
print(motorcycles)

# to remove by value
motorcycles.remove('yamaha')
print(motorcycles)

print("\n")
motorcycles = ['kawasaki', 'honda', 'yamaha', 'suzuki', 'ducati']

print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
