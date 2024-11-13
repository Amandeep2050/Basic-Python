# Checking the greatest number of three.

# Taking three numbers as input
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Checking condition for a.
if(a > b and a > c):
    print("a is the greatest number")

# Checking condition for b.
elif(b > a and b > c):
    print("b is the greatest number")

# Default condition if a and b are not greatest then c will be the greatest of three by default.
else:
    print("c is the greatest number")

print("Thank you!")