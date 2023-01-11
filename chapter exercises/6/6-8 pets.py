Pets = []


pet = {
    'Kind_of_animal': 'Dog',
    "Owners_name": "jack",
    "Breed": "Golden_retriver"
}
Pets.append(pet)

pet = {
    'Kind_of_animal': 'Dog',
    "Owners_name": 'sam',
    "Breed": "Shiba_inu"
}
Pets.append(pet)

pet = {
    'Kind_of_animal': 'Cat',
    "Owners_name": 'dilli',
    "Breed": "American_short_hair"
}
Pets.append(pet)

for pet in Pets:
    print(f"\nHere is the info about the {pet['Owners_name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")



#150
#98138
