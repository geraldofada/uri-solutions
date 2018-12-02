a, v = map(int, input().split())

test = 1
while a != 0 and v != 0:
    print("Teste {}".format(test))

    voos_aeroporto = {}

    for i in range(v):
        c, d = map(int, input().split())

        if c in voos_aeroporto:
            voos_aeroporto[c] += 1
        else:
            voos_aeroporto[c] = 1
        
        if d in voos_aeroporto:
            voos_aeroporto[d] += 1
        else:
            voos_aeroporto[d] = 1

    max_value = 0
    list_aero = []
    for v in voos_aeroporto.values():
        if v > max_value:
            max_value = v

    for k, v in voos_aeroporto.items():
        if v == max_value:
            list_aero.append(k)
    
    list_aero.sort()
    result = " ".join(map(str, list_aero)) + " "
    print(result)
    print()

    test += 1
    a, v = map(int, input().split())
