favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
#141
'''This for statement is like other for statements except that we’ve
wrapped the sorted() function around the dictionary.keys() method. This
tells Python to list all keys in the dictionary and sort that list before looping
through it. The output shows everyone who took the poll, with the names
displayed in order:'''
