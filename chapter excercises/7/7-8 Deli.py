sandwich_orders = ['normal', 'cheese_sandwich', 'vegi_sandwich', 'nonvegi_sandwhich']

finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"\n{current_sandwich.title()} is made")
    finished_sandwich.append(current_sandwich)

print("\nThe Following sandwich has been: ")
for finished_sandwich in finished_sandwich:
    print(finished_sandwich.title())
