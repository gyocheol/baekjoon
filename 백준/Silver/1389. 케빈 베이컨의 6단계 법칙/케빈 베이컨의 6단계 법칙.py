from collections import deque


def bfs(v):
    Q = deque()
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                Q.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

sum_list = []
for i in range(1, N+1):
    visited = [0] * (N+1)
    bfs(i)
    sum_list.append(sum(visited))

print(sum_list.index(min(sum_list))+1)
