a, b, c, d, e = map(int, input().split())

if a > b > c > d > e:
    print("D")
elif a < b < c < d < e:
    print("C")
else:
    print("N")