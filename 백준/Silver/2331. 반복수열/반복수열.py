def cal(x):
    result = []
    for i in str(x):
        result.append(i)
    return list(map(int, result))


def linear_search(list, key):
    for i in list:
        if key == i:
            return i
    return -1


A, P = map(int, input().split())
D = []

D.append(A)
k = 1
index = 0
while True:
    sum = 0
    s = cal(D[-1])
    for i in s:
        sum += i ** P
    if sum in D:
        # print("break! ", sum)
        index = sum
        break
    D.append(sum)
    # k += 1

for i in range(len(D)):
    if index == D[i]:
        print(i)
# print(D)
