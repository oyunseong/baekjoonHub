import sys
sys.setrecursionlimit(10000)

M, N, K = map(int, input().split())


def dfs(x, y):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[nx][ny] == 0:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = -1  # 방문 처리
                cnt += 1
                dfs(nx, ny)
    return cnt


matrix = [[1] * N for _ in range(M)]
pos = [[0] for _ in range(K)]
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for k in range(M - y2, M - y1):
        for j in range(x1, x2):
            matrix[k][j] = 0

# for i in matrix:
#     print(i)

area = []

for i in range(N):  # 가로
    for j in range(M):  # 세로
        if matrix[j][i] == 1:
            cnt = 0
            value = dfs(j, i)
            if value == 0:
                value = 1
            area.append(value)

print(len(area))
area.sort()
for i in area:
    print(i, end=' ')
