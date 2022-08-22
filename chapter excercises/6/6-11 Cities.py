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
        'Nearby': 'alaska range',
    }
}

for city, about in Cities.items():
    print(f"\n{city.title()}:")
    for info, infor in about.items():
        print(f"{info.title()} - {infor}")
