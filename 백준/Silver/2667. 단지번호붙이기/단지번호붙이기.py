from collections import deque

def bfs(x, y):
    global total
    Q = deque()
    Q.append((x, y))
    arr[x][y] = 2

    while Q:
        x, y = Q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and  arr[nx][ny] == 1:
                visited[nx][ny] = 2
                total += 1
                Q.append((nx, ny))


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

all_cnt = 0
cnt = []

for i in range(N):
    for j in range(N):
        total = 1
        if arr[i][j] and not visited[i][j]:
            bfs(i, j)
            cnt.append(total)
            all_cnt += 1

cnt.sort()
print(all_cnt)
for i in range(all_cnt):
    print(cnt[i])