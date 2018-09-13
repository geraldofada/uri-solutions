x_a1, y_a1, x_a2, y_a2 = map(int, input().split())
x_b1, y_b1, x_b2, y_b2 = map(int, input().split())

if(x_a2 < x_b1 or x_a1 > x_b2):
    print(0)
elif(y_a2 < y_b1 or y_a1 > y_b2):
    print(0)
else:
    print(1)