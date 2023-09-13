def puissance(n,p):
    tmp = n
    for _ in range(1,p):
        tmp *= n
    return tmp

print(puissance(17,1024))