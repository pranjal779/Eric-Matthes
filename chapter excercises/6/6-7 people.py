people = []

person = {
    'first_name': 'Pranjal',
    'last_name': 'Shukla',
    'age': 27,
    'city': 'New York'
    }
people.append(person)

person = {
    'first_name': 'Dillion',
    'last_name': 'harper',
    'age': 29,
    'city': 'LA'
    }
people.append(person)

person = {
    'first_name': 'Naru',
    'last_name': 'uza',
    'age': 24,
    'city': 'konha',
    }
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, belongs to {city}, thier age is {age}")


