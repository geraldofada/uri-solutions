time_play = int(input())
test = 1

while(time_play != 0):
    print("Teste", test)
    player1 = input()
    player2 = input()

    for i in range(time_play):
        play = input().split(' ')
        if( (int(play[0]) + int(play[1])) % 2 == 0):
            print(player1)
        else:
            print(player2)
    
    test += 1
    print()
    time_play = int(input())
