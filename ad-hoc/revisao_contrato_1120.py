d, n = map(str, input().split())

while d != "0" and n != "0":
    new_n = n.replace(d, "")

    if new_n != "":
        print(int(new_n))
    else:
        print("0")

    d, n = map(str, input().split())