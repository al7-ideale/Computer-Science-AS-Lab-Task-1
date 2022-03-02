#To Identify whether the number taken as input is from the USER is Armstrong or not.
#(A number is called Armstrong if the sum of cube of each digit is equal to the number entered)

num = int(input("Enter a number: "))
count = len(str(num))

sum = 0
temp = num
while temp >0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10
if num == sum:
    print(num," is a Armstrong Number")
else:
    print(num," is not a Armstrong Number")
