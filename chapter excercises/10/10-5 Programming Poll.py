filename = "programming_poll_reasons.txt"

responses = []
while True:
    response = input("\nWhy do you like programming?: ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")


"""
notice at line 6 and 5
if it was
responses = .............
responses.append(response)

it gives error
unresolved attributes reference 'append' for class 'str'

change to 
resonpse = ............. (in line 5 and it works)


"""
