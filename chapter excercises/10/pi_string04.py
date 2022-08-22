filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_stringbd = ''
for line in lines:
    pi_stringbd += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_stringbd:
    print("Your birthday appear in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
