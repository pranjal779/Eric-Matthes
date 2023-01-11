class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}.")
        print(f"\nThe cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n {self.restaurant_name} is open.")
        print("----------------")

    def des_msg_resturant(self):
        msg = f"{self.restaurant_name} serves wonderful {self.cuisine_type}"
        print(f"\n{msg}")


des_restaurant01 = Restaurant("Rupali", "Non-Veg & Veg")
des_restaurant02 = Restaurant("Jackson Hotel", "Veg Only")
des_restaurant03 = Restaurant("Ulunu Hotel", "Non-Veg & Veg")
#print(Restaurant.cuisine_type)

des_restaurant01.describe_restaurant()
des_restaurant01.open_restaurant()

des_restaurant02.describe_restaurant()
des_restaurant02.open_restaurant()


des_restaurant03.describe_restaurant()
des_restaurant03.open_restaurant()
des_restaurant03.des_msg_resturant()
