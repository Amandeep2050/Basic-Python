# To check for a list whether it is palindrome or not.

# taking a random list.
list1 = [1,2,3,2,1]
# Making its copy into a new list.
list2 = list1.copy()
# Reversing the copied list.
list2.reverse()

# Now, checking whether the reversed copy list is equal to the original one or not.
if(list1 == list2):
    print("Palindrome list") # if equal
else:
    print("Not a Palindrome list") # if not equal