filename = 'programming_03.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programing.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# I don't know why it was not working separately in write_message04,
# but maybe I had to use the file call method.
