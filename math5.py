#To Identify whether the numbers entered is positive, negative or zero.

n = int(input("Enter a number: "))
if n == 0:
    print(str(n) + " is zero")

elif n>0:
    print(str(n) + " is positive")

else:
    print(str(n) + " is negative")
