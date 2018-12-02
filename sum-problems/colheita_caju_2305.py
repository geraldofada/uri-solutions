l, c, m, n = map(int, input().split())

grade = [[0]*(c+1)]
for _ in range(l):
    l_grade = list(map(int, input().split()))
    l_grade.insert(0, 0)
    grade.append(l_grade)

# creating the integral image
im_grade = [[0 for _ in range(c+1)] for _ in range(l+1)]
for i in range(1, len(grade)):
    for j in range(1, len(grade[0])):
        im_grade[i][j] = (grade[i][j] + im_grade[i][j-1] +
                          im_grade[i-1][j] - im_grade[i-1][j-1])

# getting the max sum
max_soma = 0
for i in range(m, len(im_grade)):
    for j in range(n, len(im_grade[0])):
        soma = (im_grade[i][j] + im_grade[i-m][j-n] -
                im_grade[i][j-n] - im_grade[i-m][j])

        if soma > max_soma:
            max_soma = soma

print(max_soma)
