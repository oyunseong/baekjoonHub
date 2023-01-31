n = int(input())
dp = [0] * (n + 1)
step = [0] * (n + 1)

for i in range(1, n + 1):
    step[i] = int(input())

if n == 1:
    print(step[1])
    exit()
if n == 2:
    print(sum(step[:3]))
    exit()

dp[1] = step[1]
dp[2] = step[1] + step[2]

for i in range(3, n + 1):
    dp[i] = max(step[i] + dp[i - 2], step[i] + step[i - 1] + dp[i - 3])

print(dp[n])
