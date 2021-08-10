def show_magicians(magicians):    
    """Print the name of each magician"""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """Add the Great to the each name"""

    # A new list to add changes magicians names
    great_magicians = []    
    
    # Adding the Great to each name from the list
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)
    
    # Add the great magicians back into magicians
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['David Copperfield', 'Doug Henning', 'Lance Burton']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal list of magicians:")
show_magicians(magicians)