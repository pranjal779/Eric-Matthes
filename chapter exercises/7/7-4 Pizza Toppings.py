prompt = "Do you want to any pizza toppings?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"\nLet me add this {toppings.title()}")
    else:
        break

    
