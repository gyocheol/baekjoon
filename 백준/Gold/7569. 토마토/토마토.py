from collections import deque

def bfs():
    while Q:
        f, x, y = Q.popleft()
        for k in range(6):
            nf = f + dh[k]
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nf < H and not arr[nf][nx][ny] and not visited[nf][nx][ny]:
                visited[nf][nx][ny] = visited[f][x][y] + 1
                Q.append((nf, nx, ny))


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

Q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                Q.append((h, i, j))
                visited[h][i][j] = 1
            elif arr[h][i][j] == -1:
                visited[h][i][j] = 1

bfs()
ans = 0
flag = 1
for h in range(H):
    for i in range(N):
        for j in range(M):
            if visited[h][i][j] > ans:
                ans = visited[h][i][j]
            if visited[h][i][j] == 0:
                flag = 0

# print(visited)

if flag:
    print(ans-1)
else:
    print(-1)
