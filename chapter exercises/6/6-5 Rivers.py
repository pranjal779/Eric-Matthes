rivers = {
    'Egypt': 'nile',
    'jabalpur': 'narmada' ,
    'canada':  'fraser'
}

for country, river in rivers.items():
    print(f"the {river.title()} flows through {country.title()}.")

print("\n the follwing rivers are included in the data set.")
for river in rivers.values():
    print(f"{river.title()}")

print("\n the following cities are inclued in the data set as well.")
for river in rivers.keys():
    print(f"{river.title()}")
