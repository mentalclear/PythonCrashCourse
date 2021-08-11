alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Accessing values
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding values
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_1 = {}
alien_1['color'] = 'green'
alien_1['point'] = 5
print(alien_1)

# modifying values
alien_2 = {'color': 'green'}
print("The alien is " + alien_2['color'] + ".")

alien_2['color'] = 'yellow'
print("The alien is now " + alien_2['color'] + ".")
