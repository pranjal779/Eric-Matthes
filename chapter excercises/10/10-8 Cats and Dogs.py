filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"Reading file")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(" Sorry, I can't find that file. ")
