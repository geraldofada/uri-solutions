n = int(input())

result = 0

if n > 100:
    result += 167
    n -= 100
    result += n * 5
elif 30 < n <= 100:
    result += 27
    n -= 30
    result += n * 2
elif 10 < n <= 30:
    result += 7
    n -= 10
    result += n * 1
else:
    result = 7

print(result)