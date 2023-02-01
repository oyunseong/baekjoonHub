n = int(input())
color = []
dp = [[0 for _ in range(3)] for i in range(n)]
for i in range(n):
    color.append(list(map(int, input().split())))

for i in range(n):
    dp[i][0] = min(dp[i - 1][1] + color[i][0], dp[i - 1][2] + color[i][0])
    dp[i][1] = min(dp[i - 1][0] + color[i][1], dp[i - 1][2] + color[i][1])
    dp[i][2] = min(dp[i - 1][0] + color[i][2], dp[i - 1][1] + color[i][2])

print(min(dp[-1]))
