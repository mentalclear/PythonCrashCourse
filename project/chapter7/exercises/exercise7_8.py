sandwich_orders = ['Grilled Cheese', 'Grilled Chicken', 'BLT', 'Club', 'Reuben']
finished_sandwiches = []

while sandwich_orders:
    sandwich_made = sandwich_orders.pop()
    print("I made your " + sandwich_made + " sandwich")
    finished_sandwiches.append(sandwich_made)

print("Sandwiches made to order:")
for sandwich in finished_sandwiches:
    print(sandwich)
