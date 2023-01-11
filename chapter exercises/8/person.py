def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


def build_person_2(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person_2 = {'first': first_name, 'last': last_name}
    if age:
        person_2['age'] = age
    return person_2


musician_2 = build_person_2('jimi', 'hendrix', age=27)
print(musician_2)
