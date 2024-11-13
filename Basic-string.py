# Basics of String

# Inputing a string
Name = input("Enter Your Name: ")

# Printing length of string
print("Length of your name is: ", len(Name))

# Indexing in string
print("Value at index 4 is:",Name[4])
print("Value at index 0 is:",Name[0])

# Slicing of string
print("Sliced piece of string: ",Name[0 : 4])

# Negative indexing string
print("Negative sliced piece: ",Name[-5:-1])

# Capitalize First letter of string
print("After Capitalized First letter: ",Name.capitalize())