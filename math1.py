#To Calculate the sum of first "n" natural number.

def a():
    s = 0
    n = int(input("Till which number? "))
    for i in range(n):
        s = s + n
        n = n - 1
    print("The sum is " + str(s))


a()

