from collections import deque
import sys

input = sys.stdin.readline


def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True


def bfs(v):
    visited = [False] * (N+1)
    Q = deque()
    Q.append(v)
    visited[v] = True

    while Q:
        now = Q.popleft()
        print(now, end=' ')
        for j in graph[now]:
            if not visited[j]:
                Q.append(j)
                visited[j] = True


N, M, start = map(int, input().split())
visited = [False] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs(start)
print()
bfs(start)