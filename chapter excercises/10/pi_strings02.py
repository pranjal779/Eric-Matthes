filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string02 = ''
for line in lines:
    pi_string02 += line.strip()

print(pi_string02)
print(len(pi_string02))
