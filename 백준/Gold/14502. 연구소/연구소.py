import copy
from collections import deque


def setWallInGraph(c):
    if c == 3:
        dfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                setWallInGraph(c + 1)
                graph[i][j] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0


def dfs():
    queue = deque()
    temp_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    queue.append([nx, ny])
    c = 0
    global answer
    for i in range(N):
        c += temp_graph[i].count(0)
    answer = max(answer, c)


N, M = map(int, input().split())  # 세로, 가로
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
setWallInGraph(0)
print(answer)
