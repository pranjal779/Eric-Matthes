# page 218

from Admin_importing_file import Admin

jake = Admin("jake", "major", "jake007", "jake@email.com", "India")
jake.greet_user()
jake.describe_user()

jake_privileges = [
    "can do stuff",
    "can ban",
    "can unban",
    "can promote",
    "and other powers"
]
jake.privileges.privileges = jake_privileges

print(f"\nThe admin's {jake.first_name} has these privileges")
jake.privileges.show_privileges()
