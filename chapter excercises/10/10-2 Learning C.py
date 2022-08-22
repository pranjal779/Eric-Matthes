print("changing txt from this file: ")
with open("learning_of_pythons.txt") as file_object:
    # contentzzs = file_object.read() - works if you are not going with the below for statement
    contentzzs = file_object.readlines()

print(contentzzs)
print(file_object)


for line in contentzzs:
    """Get rid of newline, then replace Python with C."""
    line = line.rstrip()
    print(line.replace("fa", "C"))

"""
You can use rstrip() and replace() on the same line. 
This is called chaining methods. In the
following code the newline is stripped from the end 
of the line and then Python is replaced by C.
The output is identical to the code shown above.

The readlines() method returns a list containing each
 line in the file as a list item. 
Use the hint parameter to limit the number of lines 
returned. If the total number of bytes 
returned exceeds the specified number, no more lines 
are returned

The read() method returns the specified number of 
bytes from the file. Default is -1 which means the 
whole file.
"""
