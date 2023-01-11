prompt = "Ticket? whats your age?: "

while True:
    ticket  = input(prompt)
    if ticket == 'quit':
        break
    ticket = int(ticket)

    if ticket < 3:
        print("\nYout ticket is for free.")
    elif ticket < 13:
        print("\nyour ticket is $10.")
    else:
        print("your ticket is $15.")
