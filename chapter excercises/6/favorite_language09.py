favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("the following languages have been mentioned:")
for language in set (favorite_languages.values()):
    print(language.title())
'''t’s easy to mistake sets for dictionaries because they’re both wrapped in braces.
When you see braces but no key-value pairs, you’re probably looking at a set. Unlike
lists and dictionaries, sets do not retain items in any specific order.'''
