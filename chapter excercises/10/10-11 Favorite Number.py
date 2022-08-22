import json

userFavoriteNumber = input("What is your favorite number?:- ")

filename = 'userFavNumber.json'
with open(filename, 'w') as f:
    json.dump(userFavoriteNumber, f)
    # print(f"These are your fav numbers: \n{userFavoriteNumber}.")
    print({userFavoriteNumber})
