n = int(input())

for _ in range(n):
    m = int(input())
    alunos = list(map(int, input().split()))
    alunos_ord = sorted(alunos, reverse=True)

    alunos_mudados = 0
    for i, j in zip(alunos, alunos_ord):
        if i == j:
            alunos_mudados += 1

    print(alunos_mudados)
