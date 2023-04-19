from collections import deque


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = True
    total = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] and not visited[nx][ny]:
                Q.append((nx, ny))
                visited[nx][ny] = True
                total += 1
    ans_list.append(total)


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
ans_list = []
visited = [[False] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            bfs(i, j)
            ans += 1

print(ans)
ans_list.sort()
for i in ans_list:
    print(i)
