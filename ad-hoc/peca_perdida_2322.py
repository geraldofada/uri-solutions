n = int(input())
pieces = list(map(int, input().split()))

pieces.sort()
missing = 0
if n != 2:
    for i in range(1, len(pieces)):
        if pieces[i-1] + 1 != pieces[i]:
            missing = pieces[i-1] + 1
            break
        elif missing == 0 and pieces[len(pieces)-1] == n:
            missing = 1
        elif missing == 0 and pieces[len(pieces)-1] != n:
            missing = n
else:
    if pieces[0] == n:
        missing = 1
    else:
        missing = n

print(missing)