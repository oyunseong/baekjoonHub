import sys

sys.setrecursionlimit(10000)


# x:가로 y:세로
def dfs(x, y):
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)


case = int(input())
for _ in range(case):
    M, N, K = map(int, input().split())  # m : 가로 n : 세로, k : 배추
    graph = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1
    # 탐색 시작
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                dfs(i, j)
                cnt += 1

    print(cnt)
