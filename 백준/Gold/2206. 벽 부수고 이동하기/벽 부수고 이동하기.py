from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append((n-1, m-1, 0, 1))
    visited[n-1][m-1] = False
    while Q:
        x, y, block, cnt = Q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx == 0 and ny == 0:
                return cnt + 1
            elif x == 0 and y == 0:
                return cnt
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                if not block:
                    if route[nx][ny] == "1":
                        visited[nx][ny] = False
                        Q.append((nx, ny, block+1, cnt+1))
                    else:
                        visited[nx][ny] = False
                        Q.append((nx, ny, block, cnt+1))
                elif block == 1 and route[nx][ny] == "0" and visited2[nx][ny]:
                    visited2[nx][ny] = False
                    Q.append((nx, ny, block, cnt + 1))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
route = [list(input().rstrip()) for _ in range(n)]
visited = [[True] * m for _ in range(n)]
visited2 = [[True] * m for _ in range(n)]
ans = bfs()
print(ans if ans else -1)
