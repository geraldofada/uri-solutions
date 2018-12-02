r = int(input())

test = 1
while r != 0:
    print("Teste", test)
    aldo = 0
    beto = 0

    for i in range(r):
        a, b = map(int, input().split())

        aldo += a
        beto += b
    
    if aldo > beto:
        print("Aldo")
    else:
        print("Beto")
    
    print()

    test += 1
    r = int(input())