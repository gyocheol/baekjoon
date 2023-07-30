from collections import deque
def bfs(x, y):
    global ans
    Q = deque()
    Q.append((x, y))
    visited[x][y] = False

    while Q:
        xx, yy = Q.popleft()
        for k in range(4):
            nx = dx[k] + xx
            ny = dy[k] + yy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] and arr[nx][ny] != "X":
                visited[nx][ny] = False
                Q.append((nx, ny))
                if arr[nx][ny] == "P":
                    ans += 1
    return ans


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[True] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "I":
            bfs(i, j)
if ans:
    print(ans)
else:
    print("TT")