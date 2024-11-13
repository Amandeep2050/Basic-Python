# Taking marks as input
Marks = int(input("Enter your Marks: "))

# Applying different conditions
if(Marks >= 90 and Marks <=100):
    print("Grade - A")
elif(Marks >= 80 and Marks <= 90):
    print("Grade - B")
elif(Marks >= 70 and Marks <= 80):
    print("Grade - C")
elif(Marks < 70 and Marks >= 0):
    print("Grade - D")
else:
    print("Not a correct input!")
print("Thank you!")