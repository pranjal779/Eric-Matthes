import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username03.json'
    try:
        with open(filename) as x:
            username = json.load(x)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """Gree the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is yor name? ")
        filename = 'username03.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")


greet_user()
