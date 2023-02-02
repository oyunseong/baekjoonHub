# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# k = 거리
r, c, k = map(int, input().split())
visited = [[0 for _ in range(c)] for _ in range(r)]  # 2차원 배열 초기화
answer = 0  # 경우의 수
maps = [[0] * c for _ in range(r)]  # 입력 값
for i in range(r):
    maps[i] = input()  # 입력 받기


def dfs(x, y, count):
    global answer
    visited[x][y] = 1  # 방문 처리

    if count == k:
        if [x, y] == [0, c - 1]:  # 도착 지점일 때
            answer += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 지도 안쪽 + T가 아닐때
        if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and maps[nx][ny] != 'T':
            visited[nx][ny] = 1  # 방문 처리
            dfs(nx, ny, count + 1)  # dfs
            visited[nx][ny] = 0  # 방문 초기화


dfs(r - 1, 0, 1)
print(answer)
