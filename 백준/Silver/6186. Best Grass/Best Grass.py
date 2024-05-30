from collections import deque

def bfs(r, c):
    Q = deque()
    Q.append((r, c))
    visited[r][c] = True
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = dx[k]+x
            ny = dy[k]+y
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == "#" and  not visited[nx][ny]:
                visited[nx][ny] = True
                Q.append((nx, ny))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if field[i][j] == "#" and not visited[i][j]:
            ans += 1
            bfs(i, j)

print(ans)