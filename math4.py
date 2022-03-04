#To Determine the number is odd, even or neutral.

n = int(input("Enter a number: "))
if n == 0:
    print(str(n) + " is neutral")

elif n%2 == 0:
    print(str(n) + " is even")

else:
    print(str(n) + " is odd")
