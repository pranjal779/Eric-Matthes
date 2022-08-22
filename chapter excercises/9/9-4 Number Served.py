class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}.")
        print(f"\nThe cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n {self.restaurant_name} is open.")
        print("----------------")

    def serverd(self, number_served):
        self.number_served = number_served

    def increment_served(self, additional_served):
        self.number_served += additional_served


restaurantzx = Restaurant('the mean queen', 'pizza')
restaurantzx.describe_restaurant()

print(f"\nNumber served: {restaurantzx.number_served}")
restaurantzx.number_served = 430
print(f"Number served: {restaurantzx.number_served}")

restaurantzx.serverd(1257)
print(f"Number served: {restaurantzx.number_served}")

restaurantzx.increment_served(239)
print(f"Number served: {restaurantzx.number_served}")

des_restaurant01 = Restaurant("Rupali", "Non-Veg & Veg")
des_restaurant02 = Restaurant("Jackson Hotel", "Veg Only")

des_restaurant01.describe_restaurant()
des_restaurant01.open_restaurant()

des_restaurant02.describe_restaurant()
des_restaurant02.open_restaurant()

