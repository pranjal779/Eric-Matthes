name = input("What's your name? ")

filename = "guest.txt"

with open(filename, 'w') as f:
    f.write(name)

"""
xx = input()

filename = "guest_book.txt"

with open("guest_book.txt") as file_object:
    file_has = file_object.read()
    
    print("Hello" + f"{xx}")"""
