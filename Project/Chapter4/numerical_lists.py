for value in range(1, 5):  # the number 5 isn't included here
    print(value)

# Packing numbers from range() into a list
numbers = list(range(1, 6))
print(numbers)

# Only even numbers in the list
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Creating a list of squares
squares = []
for value in range(1, 11):
    # square = value ** 2       # This can be simplified
    # squares.append(square)
    squares.append(value ** 2)
print(squares)

# Simple statistcs for lists
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("\nThis is min(digits): " + str(min(digits)))
print("This is max(digits): " + str(max(digits)))
print("This is sum(digits): " + str(sum(digits)))