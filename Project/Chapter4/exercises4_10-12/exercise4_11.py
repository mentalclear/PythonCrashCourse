my_fav_pizza = ['cheese pizza', 'vegetarian pizza', 'seafood pizza']
friend_pizzas = my_fav_pizza[:]

my_fav_pizza.append('pineapple pizza')
friend_pizzas.append('meat pizza')

print("My favorite pizzas are")
for pizza in my_fav_pizza:
    print(pizza)

print("\nMy friend's favorite pizzas are")
for pizza in friend_pizzas:
    print(pizza)
