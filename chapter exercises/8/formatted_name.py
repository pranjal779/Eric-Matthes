def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_again(first_name_2, last_name_2):
    full_name_2 = f"{first_name_2} {last_name_2}"
    return full_name_2.title()


musician_2 = get_formatted_again("chester", "benington")
print(musician_2)


