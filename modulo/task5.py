def li(n):
    a = []
    b = float(n%1)
    while(n != 0):
        if b < 1.0 and b > 0.0:
            a.append(b)
            b = 0
        else:
            a.append(int(n%10))
            n//=10
    a.reverse()
    return print (a)

li(12.24)



x = 12.24

print(str(x).split(".")[1])