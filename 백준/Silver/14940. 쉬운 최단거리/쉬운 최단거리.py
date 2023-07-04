from collections import deque

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = True

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                ans[nx][ny] = ans[x][y] + 1
                arr[nx][ny] = 3
                Q.append((nx, ny))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ans[i][j] = -1
for i in range(n):
    print(*ans[i])