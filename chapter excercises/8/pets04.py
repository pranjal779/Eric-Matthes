def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

'''When you use default values, any parameter with a default value needs to be listed
after all the parameters that don’t have default values. This allows Python to continue interpreting positional argumen'''
