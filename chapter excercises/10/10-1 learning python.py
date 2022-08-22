print("...Reading the entire file: ")
with open('learning_of_pythons.txt') as file_object:
    content = file_object.read()

print(file_object)
print(content.rstrip())
print("-----------------------------------------")

print("\nLooping: ")
content01 = ''
with open('learning_of_pythons.txt') as lines:
    for line in lines:
        content01 += line.strip()
        print(line.rstrip())

print("content is: ")
print(f"\n{content01}")
print(len(content01))
print("-----------------------------------")


print("\n---- Storing the lines in a list:")
with open('learning_of_pythons.txt') as lineszzz:
    lines02 = lineszzz.readlines()
    for linez in lines02:
        print(linez.rstrip())

# for linez in lines02:
#    print(linez.rstrip())

'''anything works'''
