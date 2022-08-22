pizza = ['Margherita', 'Cheese & Corn', 'Farmhouse']

print("\nThese are my fav pizza's")
for pizzazs in pizza:
    print(f"\n{pizzazs.title()}, that was yummy!")

print("\n yuumm!")

print(f"\nI like {pizza[0].title()}, as it is so cheesy")
print(f"\nI like {pizza[1].title()}, as it has chese & Golden Corn")
print(f"\nI like {pizza[2].title()}, as it has Onion, Capsicum, Grilled Mushroom & Tomato")

friend_pizza = pizza[:]
print(friend_pizza)

pizza.append('Delux veggie')
friend_pizza.append('fresh veggie')

print(pizza)
print(friend_pizza)

print("\nMy fav pizzas are:")
for pizzazs in pizza:
    print(pizzazs)
    print("\nMy Frnd's piza")
    for pizazzs in friend_pizza:
        print(pizazzs)
