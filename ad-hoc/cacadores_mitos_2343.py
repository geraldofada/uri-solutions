occurrence = int(input())

city = {}
for i in range(occurrence):
    strike = input()
    if strike in city:
        city[strike] += 1
    else:
        city[strike] = 0

strike_counter = 0
for v in city.values():
    strike_counter += v

if strike_counter > 0:
    print('1')
else:
    print('0')