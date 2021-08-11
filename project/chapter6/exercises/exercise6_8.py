pets = {
    'sharik':{'type': 'dog',
              'owner': 'uncle feodor'},
    'matroskin':{'type': 'cat',
                 'owner': 'uncle feodor'},
    'kto tam':{'type': 'bird',
               'owner': 'uncle feodor'}
}

for pet_name, pet_data in pets.items():
    print("\nPet name: " + pet_name.title())
    print("\tPet kind: " + pet_data['type'].title())
    print("\tPet owner: " + pet_data['owner'].title())
