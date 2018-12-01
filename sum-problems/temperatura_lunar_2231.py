n, m = map(int, input().split())

test = 1
while n != 0 and m != 0:
    print("Teste {}".format(test))

    # initial temps
    temps = []
    for n in range(n):
        temps.append(int(input()))
    
    # accumulated temps
    accu_temps = [0] * len(temps) 
    accu_temps[0] = temps[0]
    for i in range(1, len(accu_temps)):
        accu_temps[i] = accu_temps[i-1] + temps[i]
    
    # checking the min and max
    sums = [int(accu_temps[m-1]/m)]
    for i in range(m, len(accu_temps)):
        sums.append(int((accu_temps[i]-accu_temps[i-m])/m))
    
    print("{} {}\n".format(min(sums), max(sums)))

    test += 1
    n, m = map(int, input().split())