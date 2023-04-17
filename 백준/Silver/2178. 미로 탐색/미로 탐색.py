from collections import deque


def bfs(a, b):
    Q = deque()
    Q.append((a, b))

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                Q.append((nx, ny))


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
bfs(0, 0)
print(arr[n-1][m-1])