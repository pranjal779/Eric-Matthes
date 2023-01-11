filename = 'alice in wonderland.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileExistsError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
