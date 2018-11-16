from functools import cmp_to_key

def comp(a, b):
    if int(a[1]) > int(b[1]):
        return 1
    elif int(a[1]) < int(b[1]):
        return -1
    if int(a[2]) > int(b[2]):
        return 1
    elif int(a[2]) < int(b[2]):
        return -1
    if int(a[3]) > int(b[3]):
        return 1
    elif int(a[3]) < int(b[3]):
        return -1
    elif a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    else:
        return 0

n = int(input())

paises = []
for _ in range(n):
    paises.append(tuple(input().split()))

paises.sort(reverse=True, key=cmp_to_key(comp))

for p in paises:
    print("{} {} {} {}".format(p[0], p[1], p[2], p[3]))