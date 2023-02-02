# 수빈 N
# 동생 K
# 수빈 위치가 X =N 일때 1초후에 X-1 X+1로 이동
# 순간이동하면 1초후에 2xX위치
# 동생찾기 시간

import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

visited = [False] * 200001

dp = [0] * 200001


def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    dp[start] = 0
    while queue:
        v = queue.popleft()
        # 현재 = 이전꺼 + 1
        if v == K:  # 수빈이 찾음
            print(dp[v])
            break
            # 뒤로    v-1
            # 앞      v+1
            # 점프     v*2

        if 0 <= v - 1 <= 100000 and not visited[v - 1]:  # -1로 갔을 때  큐에 넣고 방문 처리
            queue.append(v - 1)
            visited[v - 1] = True
            dp[v - 1] = dp[v] + 1  # 이전에 걸린 시간 +1
        if 0 <= v + 1 <= 100000 and not visited[v + 1]:
            queue.append(v + 1)
            visited[v + 1] = True
            dp[v + 1] = dp[v] + 1
        if 0 <= v * 2 <= 100000 and v * 2 <= K + 1 and not visited[v * 2]:
            queue.append(v * 2)
            visited[v * 2] = True
            dp[v * 2] = dp[v] + 1


bfs(N, visited)
