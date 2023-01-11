prompt = "what kind of topping do you want?"
prompt += "\nEnter 'quit' if you want to exit: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"\nAdding {topping.title()}.")
    else:
        break
