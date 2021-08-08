sandwich_orders = ['grilled cheese', 'pastrami', 'grilled chicken', 'pastrami', 'club', 'reuben', 'pastrami']
finished_sandwiches = []
print("Unfortunately the deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_made = sandwich_orders.pop()
    print("I made your " + sandwich_made.title() + " sandwich")
    finished_sandwiches.append(sandwich_made)

print("Sandwiches made to order:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
