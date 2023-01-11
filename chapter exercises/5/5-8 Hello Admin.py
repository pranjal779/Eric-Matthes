Admins = ['Ajax', 'Modi', 'Odin', 'Vishnu', 'Shiva', 'Zeus', 'Hades', 'Posiden']

Users = ['lexi', 'abhimanyu', 'Karna', 'Modi', 'Ajax']

for User in Users:
    if User in Admins:
        print(f"Hello admin {User}, would you like to see a status report?.")
    else:
        print(f"Hello {User}, thank you for logging in again.")

for Admin in Admins:
    if Admin not in Users:
        print(f"Hello admin {Admin}, would you like to see a status report?.")


