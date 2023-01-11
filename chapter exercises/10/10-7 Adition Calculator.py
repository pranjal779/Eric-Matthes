print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("Give me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, enter a number")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")
