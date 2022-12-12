from collections import deque


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = True
    color = arr[x][y]
    while Q:
        x, y = Q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == color:
                visited[nx][ny] = True
                Q.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

ans = [0, 0]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            ans[0] += 1

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            ans[1] += 1

print(*ans)