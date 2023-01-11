class User:
    def __init__(self, first_name, last_name, user_name, phone, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.user_name = user_name.title()
        self.phone = phone
        self.email = email

    def greet_user(self):
        print(f"\nHow are you doing {self.user_name}")

    def describe_user(self):
        print("The user info:")
        print(f"{self.first_name} {self.last_name}")
        print(f"{self.user_name}")
        print(f"{self.phone}")
        print(f"{self.email}")
        print("--------------------------")


info = User("Pranjal", "shukla", "Pranjal779", "999999", "farfa@gmail.com")
info.greet_user()
info.describe_user()

info02 = User("Adun", "shani", "shani009", "00098776", "uqyriuqrh@gmail.com")
info02.greet_user()
info02.describe_user()

info3 = User("kkd", "uuka", "Ujjka", "8295289", "cnavbs@gmail.com")
info3.greet_user()
info3.describe_user()
