guest = ['chester_beninton', 'cary', 'orin_pax', 'chris', 'taco_bell']


Message1=f"\nYou are invited to the dinner {guest[0].title()}."
Message2=f"\nYou are invited to the dinner {guest[1].title()}."
Message3=f"\nYou are invited to the dinner {guest[2].title()}."
Message4=f"\nYou are invited to the dinner {guest[3].title()}."
Message5=f"\nYou are invited to the dinner {guest[4].title()}."

party = "{} {} {} {} {}".format(Message1, Message2, Message3, Message4, Message5)
print(party)


popped_guest = guest.pop(3)
print(f"\nSadly guest {popped_guest.title()} will not be present in dinner.")
Message1=f"\nYou are invited to the dinner {guest[0].title()}."
Message2=f"\nYou are invited to the dinner {guest[1].title()}."
Message3=f"\nYou are invited to the dinner {guest[2].title()}."
Message5=f"\nYou are invited to the dinner {guest[3].title()}."

party01 = "{} {} {} {}".format(Message1, Message2, Message3, Message5)
print(party01)

guest.insert(3, 'nel')

Message1=f"\nYou are invited to the dinner {guest[0].title()}."
Message2=f"\nYou are invited to the dinner {guest[1].title()}."
Message3=f"\nYou are invited to the dinner {guest[2].title()}."
Message4=f"\nYou are invited to the dinner {guest[3].title()}."
Message5=f"\nYou are invited to the dinner {guest[4].title()}."

party02 = "{} {} {} {} {}".format(Message1, Message2, Message3, Message4, Message5)
print(party02)

print(f"\nHello found a bigger table lets go there")

guest.insert(0, 'jaxz')
guest.insert(3, 'cat_girl')
guest.append('dillion_harper')

print(guest)

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
