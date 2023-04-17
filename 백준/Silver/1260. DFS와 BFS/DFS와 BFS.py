import sys
input = sys.stdin.readline


def dfs(v):
    print(v, end=" ")
    visited[v] = True
    for j in adj[v]:
        if not visited[j]:
            dfs(j)
            visited[j]


def bfs(v):
    from collections import deque
    visited = [False] * (n+1)
    Q = deque()
    Q.append(v)
    visited[v] = True

    while Q:
        now = Q.popleft()
        print(now, end=" ")
        for j in adj[now]:
            if not visited[j]:
                Q.append(j)
                visited[j] = True


n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for i in range(n+1):
    adj[i].sort()

dfs(v)
print()
bfs(v)
