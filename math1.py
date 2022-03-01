def a():
    s = 0
    n = int(input("Till which number?"))
    for i in range(n):
        s = s + n
        n = n - 1
    print(s)


a()
