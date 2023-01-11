favorite_number = {
    'max': [23, 27, 99],
    'same': [9348, 85],
    'lilkendal': [54, 11, 31],
    'bunnyxoxo': [83, 75, 99],
    'jasmine': [78, 18, 66, 32]
}

for names, numbers in favorite_number.items():
    print(f"\n {names.title()}'s fav numbers are:")
    for number in numbers:
        print(f"- {number}")
