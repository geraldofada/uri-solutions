# time limit exceeded...

n = int(input())

compra = list(map(int, input().split()))
descarte = []
morto = []

rodada = 1
busca = 1
while busca <= n:
    if len(compra) != 0:
        if compra[0] == busca:
            morto.append(compra[0])
            del compra[0]
            busca += 1
        else:
            descarte.append(compra[0])
            del compra[0] 
    else:
        compra = descarte.copy()
        descarte = []
        rodada += 1

print(rodada)