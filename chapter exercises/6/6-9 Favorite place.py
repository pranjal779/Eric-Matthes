favorite_place = {
    'dilli': ['jabalpur', 'hastinapur', 'LA'],
    'jill': ['kanas', 'tataoon', 'ark'],
    'bill': ['jfk', 'freedomtower', 'chpshivaji airport']
}

for person, visit in favorite_place.items():
    print(f"\n{person.title()} likes to vist the following places:")
    for vist in visit:
        print(f"- {vist.title()}")
