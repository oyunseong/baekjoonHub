n = int(input())


def solution(n):
    dp = [0, 1, 1, 1]
    for i in range(n):
        dp.append(dp[-1] + dp[-3])
    print(dp[n])


solution(n)