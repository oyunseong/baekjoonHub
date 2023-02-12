# 세로, 가로
R, C = map(int, input().split())

graph = [[''] * C for _ in range(R)]
visited = [0] * 26

for i in range(R):
    string = input()
    for j in range(len(string)):
        graph[i][j] = string[j]

cnt = 1
visited[ord(graph[0][0]) - 65] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, length):
    global cnt
    cnt = max(cnt, length)  # 이동했던 거리 비교해서 큰 값저장
    # print(graph[x][y])  # 방문한 곳 출력
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if visited[ord(graph[nx][ny]) - 65] == 0:  # 미방문
                visited[ord(graph[nx][ny]) - 65] = 1  # 1로 방문표시
                dfs(nx, ny, length + 1)  # 이동 후 +1
                visited[ord(graph[nx][ny]) - 65] = 0
                # if graph[nx][ny] not in visited:
                #     visited.append(graph[nx][ny])  # 방문 표시
                # visited.pop()  # 방문 해제


dfs(0, 0, cnt)
print(cnt)
