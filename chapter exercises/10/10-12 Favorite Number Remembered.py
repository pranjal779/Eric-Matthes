import json


try:
    with open("userFavNumber.json") as uFN:
        userFavNumbs = json.load(uFN)
except FileNotFoundError:
    userFavNumbs = input("what is your Favorite Number?:- ")
    with open("userFavNumber.json", 'w') as uFN:
        json.dump(userFavNumbs, uFN)
    print("Thanks, I'll remember that.")
else:
    print(f"I know your numbers! they are {userFavNumbs}")
