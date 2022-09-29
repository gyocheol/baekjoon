def dfs(x):
    visited[x] = True
    for i in adj[x]:
        if visited[i]: continue
        visited[i] = True
        dfs(i)


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0
for i in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
# print(adj)
for i in range(1, N+1):
    if visited[i]: continue
    dfs(i)
    cnt += 1

print(cnt)