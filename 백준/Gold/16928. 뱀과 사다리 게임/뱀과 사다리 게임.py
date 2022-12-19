from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    Q = deque()
    Q.append((n, 0))
    visited[n] = True

    while Q:
        x, cnt = Q.popleft()
        if x == 100:
            print(cnt)
            break
        for k in range(6, 0, -1):
            nx = x + k
            if 1 <= nx < 101 and not visited[nx]:
                if nx in NorM:
                    visited[nx] = True
                    Q.append((arr[NorM.index(nx)][1], cnt + 1))
                    if nx == 100:
                        break
                else:
                    visited[nx] = True
                    Q.append((nx, cnt+1))
                    if nx == 100:
                        break


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N+M)]
NorM = []
for i in range(N+M):
    NorM.append(arr[i][0])
visited = [False] * 101
bfs(1)
