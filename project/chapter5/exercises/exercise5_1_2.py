cars = ['audi', 'bmw', 'subaru', 'toyota']

print("Is car in the list at position 0 == audi? I predict True")
print(cars[0] == 'audi')
print("Is car in the list at position 0 == bmw? I predict False")
print(cars[0] == 'bmw')

string_a = "This is string A"
string_b = "This is string B"

print(string_a == string_b)  # Must be False
print(string_a != string_b)  # Must be True

item_for_test = 'Apricot'
print(item_for_test == 'apricot')  # Returns False - case sensitive
print(item_for_test.lower() == 'apricot')  # This is True now they are equal

item1 = True
item2 = False
if item1 and item2 is False:
    print("All checks up")

if item1 is not True or item2 is True:
    print("All checks up")
else:
    print("This is the result otherwise")

if True:
    print("It's True!")

# Some more on conditions the python way
print("\n")
test1 = True
if test1:
    print("It's True")

if test1 is not True:
    print("Not happening")
else:
    print("Condition is Not True == False")

print(test1 is True)
