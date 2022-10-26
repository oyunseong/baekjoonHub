import sys

input = sys.stdin.readline

n = int(input())
result = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            result[i][j] = 1

s = 0
for i in range(100):
    s += result[i].count(1)

print(s)
