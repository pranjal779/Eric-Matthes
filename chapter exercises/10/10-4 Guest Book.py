filename = "guest_book.txt"

print("Enter quit when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as guest_entry_record:
            guest_entry_record.write(f"{name}\n")
        print(f"hi {name}, you've been added to the guest book.")
