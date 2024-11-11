# Swaping without third variable.

# taking input
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# performing opeation
a = a + b  
b = a - b
a = a - b

# printing result
print("After swaping:- ")
print("a = ", a)
print("b = ", b)