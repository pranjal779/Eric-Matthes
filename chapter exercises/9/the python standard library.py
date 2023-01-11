# Page 218

from random import randint
from random import choice

print(randint(1, 6))


players = ['charles', 'martina', 'florence', 'eli']
print(players)

first_up = choice(players)
print(first_up)

"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default 
value of 6. Write a method called roll_die() that prints a random number 
between 1 and the number of sides the die has. Make a 6-sided die and roll it 
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 
five letters. Randomly select four numbers or letters from the list and print a 
message saying that any ticket matching these four numbers or letters wins a 
prize.
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
Write a loop that keeps pulling numbers until your ticket wins. Print a message 
reporting how many times the loop had to run to give you a winning ticket.
9-16. Python Module of the Week: One excellent resource for exploring the 
Python standard library is a site called Python Module of the Week. Go to 
https://pymotw.com/ and look at the table of contents. Find a module that 
looks interesting to you and read about it, perhaps starting with the random
module.
"""
