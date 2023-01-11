import json

filename = "userFavNumber.json"
with open(filename) as f:
    userFavnumbs = json.load(f)

print(f"I Know yor favorite number! it's {userFavnumbs}.")


"""def readsNumber():
    """"""Get stored Number if available.""""""
    filename = 'userFavNumber.json'
    try:
        with open(filename) as u:
            userFavnum = json.load(u)
    except FileNotFoundError:
        return None
    else:
        return userFavnum
"""
