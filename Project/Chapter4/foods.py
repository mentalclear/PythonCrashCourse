my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# direct assignment will not copy the list it will assign another
# variable to the same list
# friend_foods = my_foods

# changing lists to see they are different
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
