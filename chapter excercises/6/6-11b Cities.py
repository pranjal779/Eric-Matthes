Cities = {
    'Jabalpur': {
        'Country': 'India',
        'Population': 1_268_000,
        'Important Mark': 'Narmada river'
    },

    'Anciet_Greece': {
        'Country': 'Greece',
        'Population': 3_500_000,
        'Important Mark': 'Temple of Zeus'
    },

    'talkeetna': {
        'Country': 'United States',
        'Population': 876,
        'Important Mark': 'alaska range',
    }
}

for city, about in Cities.items():
    Country = about['Country'].title()
    Population = about['Population']
    Important_Mark = about['Important Mark'].title()


    print(f"\n{city.title()} is is {Country}.")
    print(f"it has a poplutation of about {Population}.")
    print(f"{Important_Mark} is a pretty place.")


