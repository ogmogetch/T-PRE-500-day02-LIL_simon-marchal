# i=1
# j=1
# x=1
# pi=0
# q = 1000

# while q != 0 :

#     x=pi
#     pi= pi + j*(4/i)
#     j=-j
#     i+=2
#     q -= 1
# print (round(pi, 6))


pi = 0
a = 1
for i in range(1, 1000000, 2):
    pi += (4/i) * a
    a *= -1
print(round(pi, 6))