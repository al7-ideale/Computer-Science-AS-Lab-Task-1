#To Display the mathematical multiplication table of a number provided by tthe user.
n = int(input("Enter a number: "))
print("The multiplication table of " + str(n) + " is:")
for i in range(1,11):
    mult = n * i
    print(str(n) + " x " + str(i) + " = " +str(mult))