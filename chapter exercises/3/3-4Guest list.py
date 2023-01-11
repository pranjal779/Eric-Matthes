guest = ['chester_beninton', 'cary', 'orin_pax', 'chris', 'taco_bell']


Message1=f"\nYou are invited to the dinner {guest[0].title()}."
Message2=f"\nYou are invited to the dinner {guest[1].title()}."
Message3=f"\nYou are invited to the dinner {guest[2].title()}."
Message4=f"\nYou are invited to the dinner {guest[3].title()}."
Message5=f"\nYou are invited to the dinner {guest[4].title()}."

party = "{} {} {} {} {}".format(Message1, Message2, Message3, Message4, Message5)
print(party)
