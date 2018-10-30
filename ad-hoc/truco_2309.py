test = int(input())

a = 0
b = 0

for i in range(test):
    cards = list(map(int, input().split()))

    cards_a = cards[:3]
    cards_b = cards[3:]
    temp_a = 0
    temp_b = 0

    for i in range(3):
        if cards_a[i] == 12:
            cards_a[i] -= 2
        if cards_b[i] == 12:
            cards_b[i] -= 2
        if 1 <= cards_a[i] <= 3:
            cards_a[i] += 13
        if 1 <= cards_b[i] <= 3:
            cards_b[i] += 13
        
        if cards_a[i] >= cards_b[i]:
            temp_a += 1
        else:
            temp_b += 1
    
    if temp_a > temp_b:
        a += 1
    else:
        b += 1

print(a, b)