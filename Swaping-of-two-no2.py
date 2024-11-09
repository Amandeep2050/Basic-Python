# Swaping without third variable.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a = a + b
b = a - b
a = a - b
print("After swaping:- ")
print("a = ", a)
print("b = ", b)