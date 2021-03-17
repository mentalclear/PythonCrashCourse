motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])  # Creates list index out of range

# Recommended approach is to use -1 to get last element
print(motorcycles[-1].title())

motorcars = []
if len(motorcars) > 0:
    print(motorcars[-1])  # Will produce an error if accesses a null length list
else:
    print("No items in the motrocars variable")


