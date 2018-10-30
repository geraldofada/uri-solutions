from math import sqrt

l, a, p, r = map(int, input().split())

h = 0

if ((sqrt(l**2 + a**2) <= 2*r) and
    (sqrt(l**2 + p**2) <= 2*r) and
    (sqrt(p**2 + a**2) <= 2*r)):
    print("S")
else:
    print("N")
