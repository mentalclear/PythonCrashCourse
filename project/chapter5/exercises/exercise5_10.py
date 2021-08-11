current_users = ['John', 'user1', 'tester2', 'ADMIN', 'user2']
new_users = ['JOHN', 'admin', 'josh', 'jason', 'Claude']

# Creating a list of lower cased items for current users list
lowered_list = [lower_cased.lower() for lower_cased in current_users]
for name in new_users:
    if name.lower() in lowered_list:
        print("The username is already present! Please create a new username!")
    else:
        print("The user name is available")
