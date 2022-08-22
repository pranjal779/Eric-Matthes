import json


def greet_user():
    """Greet the user by name."""
    filename = 'username02.json'
    try:
        with open(filename) as f:
            username02 = json.load(f)
    except FileNotFoundError:
        username02 = input("what is your name? ")
        with open(filename, 'w') as f:
            json.dump(username02, f)
            print(f"We'll remember you when you come back, {username02}!")
    else:
        print(f"Welcome back, {username02}!")


greet_user()
