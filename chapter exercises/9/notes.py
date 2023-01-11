"""
Making an object from a class is called instantiation, and you work with
instances of a class. In this chapter you’ll write classes and create instances
of those classes. You’ll specify the kind of information that can be stored in
instances, and you’ll define actions that can be taken with these instances.
"""

"""
pg 211
Modeling Real-World Objects
As you begin to model more complicated things like electric cars, you’ll 
wrestle with interesting questions. Is the range of an electric car a property 
of the battery or of the car? If we’re only describing one car, it’s probably 
fine to maintain the association of the method get_range() with the Battery
class. But if we’re describing a manufacturer’s entire line of cars, we probably want to move get_range() to the ElectricCar class. The get_range() method 
would still check the battery size before determining the range, but it would 
report a range specific to the kind of car it’s associated with. Alternatively, 
we could maintain the association of the get_range() method with the battery but pass it a parameter such as car_model. The get_range() method would 
then report a range based on the battery size and car model.
This brings you to an interesting point in your growth as a programmer. When you wrestle with questions like these, you’re thinking at a higher 
logical level rather than a syntax-focused level. You’re thinking not about 
Python, but about how to represent the real world in code. When you reach 
this point, you’ll realize there are often no right or wrong approaches to 
modeling real-world situations. Some approaches are more efficient than 
others, but it takes practice to find the most efficient representations. If 
your code is working as you want it to, you’re doing well! Don’t be discouraged if you find you’re ripping apart your classes and rewriting them several 
times using different approaches. In the quest to write accurate, efficient 
code, everyone goes through this process.
"""
