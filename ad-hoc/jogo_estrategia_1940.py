j, r = map(int, input().split())

plays = list(map(int, input().split()))

sum_plays = []
for i in range(j):
    soma = 0
    for k in range(0 + i, len(plays), j):
        soma += plays[k]

    sum_plays.append(soma)

max_val = 0
max_id = 0
for i in range(len(sum_plays)):
    if sum_plays[i] >= max_val:
        max_val = sum_plays[i]
        max_id = i

print(max_id + 1)
