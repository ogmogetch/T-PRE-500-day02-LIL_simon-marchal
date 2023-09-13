def sum(n):
    a = 0
    while(n != 0):
        a = a + (n%10)
        n //= 10
    return print (a)

sum(44490320097)
