initial_money, operations = map(int, input().split())

players = {
    'D': initial_money,
    'E': initial_money,
    'F': initial_money
}

for i in range(operations):
    command = input().split()

    if command[0] == 'C':
        players[command[1]] -= int(command[2])
    elif command[0] == 'V':
        players[command[1]] += int(command[2])
    elif command[0] == 'A':
        players[command[1]] += int(command[3])
        players[command[2]] -= int(command[3])

print("{} {} {}".format(
    players['D'],
    players['E'],
    players['F']
))