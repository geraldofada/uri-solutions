n = int(input())

test = 1
while n != 0:
    print("Teste", test)

    people = list(map(int, input().split()))

    for i in range(len(people)):
        if people[i] == i + 1:
            print(people[i])
            print()
            break

    test += 1
    n = int(input())