def make_sandwich(*ingredients):
    """Print the list of sandwitch ingredients that have been requested."""
    print("\nMaking a sandwich with the following toppings:")
    for ingredient in ingredients:
        print(f"-{ingredient}")

make_sandwich('italian bread', 'turkey', 'swiss cheese', 'lettice', 'cucumbers', 'tomatoes')
make_sandwich('wheat bread', 'roast beef', 'american cheese', 'lettice', 'pickles')
make_sandwich('white bread', 'chicken', 'spinach', 'pickles', 'onions')
