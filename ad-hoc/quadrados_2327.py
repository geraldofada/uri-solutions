n = int(input())

quad = []
for i in range(n):
    quad.append(list(map(int, input().split())))

aux_cols = -1
for i in range(len(quad)):
    cols = 0
    for j in range(len(quad)):
        cols += quad[j][i]
    if cols == aux_cols or aux_cols == -1:
        aux_cols = cols
    else:
        aux_cols = -1
        break

aux_lines = -1
for i in range(len(quad)):
    lines = 0
    for j in range(len(quad)):
        lines += quad[i][j]
    if lines == aux_lines or aux_lines == -1:
        aux_lines = lines
    else:
        aux_lines = -1
        break

diag_1 = 0
for i in range(len(quad)):
    for j in range(len(quad)):
        if i == j:
            diag_1 += quad[i][j]

diag_2 = 0
for i in range(len(quad)):
    for j in range(len(quad)):
        if (i + j) + 1 == len(quad):
            diag_2 += quad[i][j]

if aux_cols == aux_lines == diag_1 == diag_2:
    print(aux_cols)
else:
    print('-1')