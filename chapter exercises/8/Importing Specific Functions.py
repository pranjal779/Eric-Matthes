"""
form module_name import function_name

ou can import as many functions as you want from a module by separating each function’s name with a comma:

from module_name import function_0, function_1, function_2

"""

from pizza_3 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''from module_name import function_name as fn'''
