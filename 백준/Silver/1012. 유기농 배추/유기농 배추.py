def bfs(x, y):
    from collections import deque
    Q = deque()
    Q.append((x, y))
    visited[x][y] = True

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                Q.append((nx, ny))


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    arr = [[False] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    ans = 0
    for i in range(k):
        b, a = map(int, input().split())
        arr[a][b] = True
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                bfs(i, j)
                ans += 1
    print(ans)