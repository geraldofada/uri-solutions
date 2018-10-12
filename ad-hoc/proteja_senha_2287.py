times = int(input())

def frequency(lst):
    return max(lst, key=lst.count)

test = 1
while(times != 0):
    print("Teste {}".format(test))

    password_numbers = [[], [], [], [], [], []]
    for i in range(times):
        password = {}
        list_input = list(input().split())
        password['A'] = [list_input[0], list_input[1]]
        password['B'] = [list_input[2], list_input[3]]
        password['C'] = [list_input[4], list_input[5]]
        password['D'] = [list_input[6], list_input[7]]
        password['E'] = [list_input[8], list_input[9]]

        j = 0
        for letter in list_input[10:]:
            for num in password[letter]:
                password_numbers[j].append(num)
            j += 1
    
    final = []
    for passw in password_numbers:
        final.append(frequency(passw))
    
    print("{} {} {} {} {} {} \n".format(
        final[0],
        final[1],
        final[2],
        final[3],
        final[4],
        final[5],
    ))

    test += 1
    times = int(input())
