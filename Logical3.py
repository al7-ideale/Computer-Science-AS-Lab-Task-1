#To Determine whether the student passed or failed the test of two subjects only.

print("Enter the marks in Mathematics: ")
m = int(input())
print("Enter the marks in Physics: ")
p = int(input())

if m >= 40 and p >= 40:
    print("The student passed in both Mathematics and Physics.")
    
elif m >= 40 and p < 40:
    print("The student passed in Mathematics but failed in Physics.")

elif m < 40 and p >= 40:
    print("The student passed in Physics but failed in Mathematics.")
else:
    print("The student failed in both Mathematics and Physics.")
 