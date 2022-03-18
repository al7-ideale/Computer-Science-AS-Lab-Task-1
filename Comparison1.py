#To Display the larger number among the numbers (at least 2) entered by the user and by how much.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x > y:
    print(x,"is greater than",y,"by",x-y)
else:
    print(y,"is greater than ",x,"by",y-x)
