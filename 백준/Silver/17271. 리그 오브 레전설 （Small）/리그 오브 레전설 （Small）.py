import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dp = [1] * 10001

if m == 2:
    dp[2] = 2

for i in range(m, n + 1):
    dp[i] = dp[i - 1] + dp[i - m]

print(dp[n] % 1000000007)