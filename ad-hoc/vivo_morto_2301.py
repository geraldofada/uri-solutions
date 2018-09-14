player_count, rounds = map(int, input().split())

test = 1
while(player_count != 0 and rounds != 0):
    print("Teste {}".format(test))
    player = input().split()

    for i in range(rounds):
        command = input().split()

        for j in range(2, len(command)):
            if command[1] != command[j]:
                player[j - 2] = 'out'
        
        player = list(filter(lambda p: p != 'out', player))

    print(player[0])
    print()
    test += 1
    player_count, rounds = map(int, input().split())
