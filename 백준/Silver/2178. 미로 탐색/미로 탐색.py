from collections import deque

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                Q.append((nx, ny))

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
bfs(0, 0)
print(arr[N-1][M-1])