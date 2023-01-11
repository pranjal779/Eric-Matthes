guest = ['Jaxz', 'chester_beninton', 'cary', 'cat_girl', 'orin_pax', 'nel', 'taco_bell', 'dillion_harper']

Message1=f"\nYou are invited to the dinner {guest[0].title()}."
Message2=f"\nYou are invited to the dinner {guest[1].title()}."
Message3=f"\nYou are invited to the dinner {guest[2].title()}."
Message4=f"\nYou are invited to the dinner {guest[3].title()}."
Message5=f"\nYou are invited to the dinner {guest[4].title()}."
Message6=f"\nYou are invited to the dinner {guest[5].title()}."
Message7=f"\nYou are invited to the dinner {guest[6].title()}."
Message8=f"\nYou are invited to the dinner {guest[7].title()}."

party03 = "{} {} {} {} {} {} {} {}".format(Message1, Message2, Message3, Message4, Message5, Message6, Message7, Message8)
print(party03)

popped_guest = guest.pop(0)
print(f"\nParty over for you, {popped_guest} hope you enjoyed.")

popped_guest = guest.pop(1)
print(f"\nParty over for you, {popped_guest} hope you enjoyed.")

popped_guest = guest.pop(0)
print(f"\nParty over for you, {popped_guest} hope you enjoyed.")

popped_guest = guest.pop(1)
print(f"\nParty over for you, {popped_guest} hope you enjoyed.")

popped_guest = guest.pop(1)
print(f"\nParty over for you, {popped_guest} hope you enjoyed.")

popped_guest = guest.pop(1)
print(f"\nParty over for you, {popped_guest} hope you enjoyed.")

print(guest)

Mzzg1 = f"\nyou are still invited, {guest[0].title()} Let the party begin"
Mzzg2 = f"\nyou are still invited, {guest[1].title()} Let the party begin"

party04 = "{} {}".format(Mzzg1, Mzzg2)
print(party04)

print(f"\n3am party over.")



print(guest)


print(len(guest))
