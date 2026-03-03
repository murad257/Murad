def sirala(a, b, c):
    if a <= b and a <= c:
        if b <= c:
            print(a, b, c)
        else:
            print(a, c, b)

    elif b <= a and b <= c:
        if a <= c:
            print(b, a, c)
        else:
            print(b, c, a)

    else:
        if a <= b:
            print(c, a, b)
        else:
            print(c, b, a)
x = int(input("1-ci ədəd: "))
y = int(input("2-ci ədəd: "))
z = int(input("3-cü ədəd: "))
sirala(x, y, z)
