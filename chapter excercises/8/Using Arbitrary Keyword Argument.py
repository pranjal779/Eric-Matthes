# 186
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'eistein',
                             location='princeton',
                             field='physics')

print(user_profile)

"""
The definition of build_profile() expects a first and last name, and 
then it allows the user to pass in as many name-value pairs as they want. The 
double asterisks before the parameter **user_info cause Python to create 
an empty dictionary called user_info and pack whatever name-value pairs 
it receives into this dictionary. Within the function, you can access the key value pairs in user_info just as you would for any dictionary.
    
    In the body of build_profile(), we add the first and last names to the 
user_info dictionary because we’ll always receive these two pieces of information from the user u, and they haven’t been placed into the dictionary 
yet. Then we return the user_info dictionary to the function call line.
    
    We call build_profile(), passing it the first name 'albert', the last 
name 'einstein', and the two key-value pairs location='princeton' and 
field='physics'. output.
"""
