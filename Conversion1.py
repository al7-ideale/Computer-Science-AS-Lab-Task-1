#To Count the number of digits in the number input by user.
#(Using the conversion from number to string)

number = int(input("Enter a number: "))
string_number = (str(number))
count = len(string_number)
print("The number of digits in the number is",count)
