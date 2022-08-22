players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

#looping through a slice
print("Here are the first three players in my team:")
for player in players[:3]:
    print(player.title())
