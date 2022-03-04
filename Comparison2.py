#To Display the length of each names provided by user and
#display the longest name with the number of alphabets.

# creating an empty list

names = []
 
n = int(input("Enter the number of names : "))
 
for i in range(0, n):
    new_name = str(input())
 
    names.append(new_name)
longest_name = max(names, key=len)
print("The longest name is",longest_name,"with",len(longest_name),"alphabets.")
