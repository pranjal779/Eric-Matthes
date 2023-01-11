every = ['Mount chillard', 'naruto', 'jabalpur', 'planes', 'abroad', 'mobiles']

print(every)
print(every[4])
print(every[3].title())

message = f"fav anime tv series is {every[1].title()}."
print(message)

every.append('memes')
print(every)

every.insert(0, 'twitter')
print(every)

del every[4]
print(every)

popped_every = every.pop(5)
print(every)
print(popped_every)

every.insert(3, 'xyz')
every.insert(8, 'zzzz')
every.insert(5, 'uuu')
print(every)

every.remove('xyz')
print(every)

no_fun = 'zzzz'
every.remove(no_fun)
print(every)
print(f"\nThis {no_fun.title()} is no fun anymore.")

print(f"\nThis is sorted version of the list:")
every.sort()
print(every)

print(f"\nTemporary sorted list:")
print(sorted(every))

print(f"\nPrinting list in reverse:")
print(every)

every.reverse()
print(every)


print(f"\nFindind the lenght of a list:")
print(len(every))

print()










