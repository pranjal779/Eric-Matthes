lists = ['car', 'bike', 'motorcycle', 'jets']

message1 = f"I already own a {lists[0].title()}."
message2 = f"It is a nostalgic feeling of riding my {lists[1].title()}, it reminds me of GTA sananderas starting mission."
message3 = f"I wish to ride my {lists[2].title()}again."
message4 = f"I would to go 0G on a{lists[3].title()}."

Message = "{} \n{} \n{} \n{}".format(message1, message2, message3, message4)

print(Message)
#check new line \n thing
