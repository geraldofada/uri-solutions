times = int(input())

test = 1
while(times != 0):
    print("Teste {}".format(test))

    password_numbers = []
    for i in range(times):
        password = {}
        list_input = list(input().split())
        password['A'] = [list_input[0], list_input[1]]
        password['B'] = [list_input[2], list_input[3]]
        password['C'] = [list_input[4], list_input[5]]
        password['D'] = [list_input[6], list_input[7]]
        password['E'] = [list_input[8], list_input[9]]

        pass_temp = []
        for letter in list_input[10:]:
            pass_temp.append(password[letter])
        password_numbers.append(pass_temp)

        # sei lá né mano...
        
    print(password_numbers)
    test += 1
    times = int(input())
