from collections import deque


def bfs():
    while Q:
        x, y = Q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                arr[nx][ny] = 1
                Q.append((nx, ny))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


Q = deque()
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            Q.append((i, j))
            visited[i][j] = 1
        elif arr[i][j] == -1:
            visited[i][j] = 1

bfs()

flag = 1
ans = 0
for ii in range(M):
    for jj in range(N):
        if not visited[ii][jj]:
            flag = 0
    if max(visited[ii]) > ans:
        ans = max(visited[ii])

if flag:
    print(ans-1)
else:
    print(-1)