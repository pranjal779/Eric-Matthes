# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
     "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

'''We begin at line2 with a dictionary that holds information about a
pizza that has been ordered. One key in the dictionary is 'crust', and
the associated value is the string 'thick'. The next key, 'toppings', has a
list as its value that stores all requested toppings. At line8 we summarize the
order before building the pizza. When you need to break up a long line
in a print() call, choose an appropriate point at which to break the line
being printed, and end the line with a quotation mark. Indent the next
line, add an opening quotation mark, and continue the string. Python
will automatically combine all of the strings it finds inside the parentheses.
To print the toppings, we write a for loop line11. To access the list of
toppings, we use the key 'toppings', and Python grabs the list of toppings
from the dictionary.
'''
