restaurant_foods = ('sandwich', 'salad', 'main dish', 'desert', 'drink')
for food in restaurant_foods:
    print(food)

# restaurant_foods[0] = 'burger'  Will not be able to change
print("\nMenu change happened, now dishes are")
restaurant_foods = ('burger', 'salad', 'main dish', 'ice cream', 'drink')
for food in restaurant_foods:
    print(food)
