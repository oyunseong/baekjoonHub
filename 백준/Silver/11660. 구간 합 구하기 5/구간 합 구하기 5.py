import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
data = [[0]] * (n + 1)

for i in range(1, n + 1):
    data[i] = data[i] + list(map(int, input().split()))

sum = 0
for i in range(1, n + 1):
    sum = 0
    for j in range(1, n + 1):
        sum += data[i][j]
        dp[i][j] = sum + dp[i - 1][j]

for _ in range(1, m + 1):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(data[x1][y1])
    else:
        print(dp[x2][y2] - dp[x1-1][y2] + dp[x1-1][y1-1] - dp[x2][y1-1])
