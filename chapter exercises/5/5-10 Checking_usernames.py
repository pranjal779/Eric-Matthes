Current_users = ['AMAL', 'jhon', 'torn', 'jake', 'josh']
New_users = ['Braun', 'Jhon', 'Torn', 'amal', 'peti']

Current_users_lower = [user.lower() for user in Current_users]

for New_user in New_users:
    if New_user.lower() in Current_users_lower:
        print(f"Sorry {New_user} is taken.")
    else:
        print(f"Great {New_user} is available.")
