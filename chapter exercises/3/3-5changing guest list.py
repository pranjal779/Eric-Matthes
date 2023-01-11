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
