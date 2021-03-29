family = {
             'dkilishek': {
                 'first_name': 'dmitrii',
                 'last_name': 'kilishek',
                 'age': 42,
                 'city': 'Sterling',
             },
             'tkilishek': {
                 'first_name': 'tatiana',
                 'last_name': 'kilishek',
                 'age': 45,
                 'city': 'sterling',
             },
             'mkilishek': {
                 'first_name': 'mikhail',
                 'last_name': 'kilishek',
                 'age': 17,
                 'city': 'sterling',
             },
             'akilishek': {
                 'first_name': 'aleksander',
                 'last_name': 'kilishek',
                 'age': 45,
                 'city': 'sterling',
             },
         }
for username, user_data in family.items():
    print('\nUsername: ' + username)
    full_name = user_data['first_name'] + " " + user_data['last_name']
    print("\tFull name: " + full_name.title())
    print("\tAge: " + str(user_data['age']))
    print("\tLocation: " + user_data['city'].title())
