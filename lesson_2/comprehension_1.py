munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

total_age = 0

for name, attributes in munsters.items():
    if attributes['gender'] == 'male':
        total_age += attributes['age']

print(f"Using an ordinary loop, the total age of male members is {total_age}.")

total_age = 0

male_ages = [attributes['age'] for attributes in munsters.values() if attributes['gender'] == 'male']
total_age = sum(male_ages)

print(f"Using a comprehension, the total age of male members is still{total_age}.")


    