class User:
    def __init__(self, first_name, last_name, user_name, phone, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.user_name = user_name.title()
        self.phone = phone
        self.email = email
        self.login_attempts = 0

    def greet_user(self):
        print(f"\nHow are you doing {self.user_name}")

    def describe_user(self):
        print("The user info:")
        print(f"{self.first_name} {self.last_name}")
        print(f"{self.user_name}")
        print(f"{self.phone}")
        print(f"{self.email}")
        print("--------------------------")

    def Increment_login_attempts(self):
        self.login_attempts += 1

    def Reset_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, user_name, phone, email):
        """Initialize the admin"""
        super().__init__(first_name, last_name, user_name, phone, email)
        self.privileges = []

    def show_privileges(self):
        print("\nPrvileges:")
        for privileges in self.privileges:
            print(f"-{privileges}")


eric = User("eric", "matthes", "e_matthes", "e_matthes@ex.com", "asdasdfa")
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts.....")
eric.Increment_login_attempts()
eric.Increment_login_attempts()
eric.Increment_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")

print("Resetting login attempts....")
eric.Reset_attempts()
print(f"  Login attempts: {eric.login_attempts}")

info = User("Pranjal", "shukla", "Pranjal779", "999999", "farfa@gmail.com")
info.greet_user()
info.describe_user()

info02 = User("Adun", "shani", "shani009", "00098776", "uqyriuqrh@gmail.com")
info02.greet_user()
info02.describe_user()

info3 = User("kkd", "uuka", "Ujjka", "8295289", "cnavbs@gmail.com")
info3.greet_user()
info3.describe_user()

sam = Admin('sam', 'xxx', 'i_sam', "98972461", "sam@g.com")
sam.describe_user()

sam.privileges = [
    'can reset passwords'
    'can moderate discussions'
    'can suspend accounts'
]

sam.show_privileges()
