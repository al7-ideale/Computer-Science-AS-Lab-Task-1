#To Display whether the students can drive a car or not.
#(Given: Driving is allowed if student is above 18 years and pass the license test)

age = int(input("Enter the student's age: "))
if age < 19:
    print("The student cannot drive the car.")
else:
    print("Has the student passed the license test? y/n ")

test = str(input())
if test == "y" :
    print("The student can drive the car.")
else:
    print("The student cannot drive the car.")
    