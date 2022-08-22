even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)


print(squares)

for value in range (1, 6):
    squares.append(value**2)

print(squares)

#list compreshension
squares = [value**2 for value in range(1,11)]
print(squares)

#98
