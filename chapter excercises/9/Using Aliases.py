"""

As you saw in Chapter 8, aliases can be quite helpful when using modules
to organize your projects’ code. You can use aliases when importing classes
as well.
As an example, consider a program where you want to make a bunch
of electric cars. It might get tedious to type (and read) ElectricCar over and
over again. You can give ElectricCar an alias in the import statement:
-> from electric_car import ElectricCar as EC
Now you can use this alias whenever you want to make an electric car:
-> my_tesla = EC('tesla', 'roadster', 2019)

"""
