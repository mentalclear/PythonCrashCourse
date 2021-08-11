alien_color = ['green', 'yellow', 'red']

current_alien_color = alien_color[-1]

# Multiple elif statement variation
if current_alien_color == 'green':
    print("Player has earned 5 points")
elif current_alien_color == 'yellow':
    print("Player has earned 10 points")
elif current_alien_color == 'red':
    print("Player has earned 15 points")
else:
    print("Incorrect color selected")