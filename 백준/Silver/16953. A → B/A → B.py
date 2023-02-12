a, b = map(int, input().split())

result = str(b)
cnt = 1
while result != a:
    # print(result)
    if int(result) <= a:
        if result != a:
            print("-1")
            exit()
    r = str(result)
    if r[-1] == "1":
        result = int(r[0:-1])
        cnt += 1
    elif int(result) % 2 == 0:
        result = int(result) // 2
        cnt += 1
    else:
        print("-1")
        exit()

print(cnt)
