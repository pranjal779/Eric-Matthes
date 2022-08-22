# 184
def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message011 in messages:
        print(message011)


def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_message."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["hll", "jww", ";)"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
