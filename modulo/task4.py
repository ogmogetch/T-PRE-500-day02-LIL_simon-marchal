def li(n):
    a = []
    while(n != 0):
        a.append(int(n%10))
        n //= 10
    a.reverse()
    return print (a)

li(12.24)
