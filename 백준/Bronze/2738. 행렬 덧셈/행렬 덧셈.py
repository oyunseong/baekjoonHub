N, M = map(int, input().split())

matrixA = [[] * M for _ in range(N)]
matrixB = [[] * M for _ in range(N)]

for i in range(N):
    matrixA[i] = list(map(int, input().split()))

for i in range(N):
    matrixB[i] = list(map(int, input().split()))


def add(arr1, arr2):
    _result = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            _result[i][j] += matrixA[i][j] + matrixB[i][j]
    return _result


result = add(matrixA, matrixB)
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end=' ')
    print("")
