import sys

input = sys.stdin.readline

ans, x, y = -1, 0, 0
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if arr[j] > ans:
            ans = arr[j]
            x = i + 1
            y = j + 1

print(ans)
print(x, y)
