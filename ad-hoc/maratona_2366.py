n, m = map(int, input().split())
points = list(map(int, input().split()))

points.append(42195)

ok = True
for i in range(len(points) - 1):
    if points[i+1] - points[i] > m:
        ok = False
        break

if ok:
    print("S")
else:
    print("N")