import sys
input = sys.stdin.readline

def dfs(s):
    for i in tree[s]:
        if not visited[i]:
            visited[i] += 1
            dfs(i)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    dfs(1)
    print(sum(visited)-1)