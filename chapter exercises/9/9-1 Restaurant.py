class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}.")
        print(f"\nThe cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n {self.restaurant_name} is open.")
        print("----------------")


des_restaurant01 = Restaurant("Rupali", "Non-Veg & Veg")
des_restaurant02 = Restaurant("Jackson Hotel", "Veg Only")

des_restaurant01.describe_restaurant()
des_restaurant01.open_restaurant()

des_restaurant02.describe_restaurant()
des_restaurant02.open_restaurant()
