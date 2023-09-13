def pi(x):
    a = 1
    for i in range (x, 0, -1):
        a = 6 + (i * 2 - 1)**2 / a
    return (a - 6)

print(pi(999))