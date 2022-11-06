from collections import deque

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    arr[x][y] = 0

    while Q:
        x, y = Q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny]:
                arr[nx][ny] = 0
                Q.append((nx, ny))

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    cnt = 0

    for _ in range(K):
        a, b = map(int, input().split())
        # 반대로 넣어줘야함
        arr[b][a] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)