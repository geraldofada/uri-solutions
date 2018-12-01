l, c, m, n = map(int, input().split())

grade = []
for _ in range(l):
    l_grade = list(map(int, input().split()))
    grade.append(l_grade)

max_soma = 0

# take the first index of each sub matrix
for i in range(0, l, m):
    for j in range(0, c, n):

        # iter through each sub matrix
        # starting at its first index
        soma = 0
        for k in range(i, m + i):
            for l in range(j, n + j):
                soma += grade[k][l]
        
        if soma > max_soma:
            max_soma = soma

print(max_soma)