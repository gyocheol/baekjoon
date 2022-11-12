from collections import deque

def bfs(x):
    visited = [0] * 100001
    Q = deque()
    Q.append(x)
    while Q:
        x = Q.popleft()
        if x == K:
            return visited[x]
        else:
            for i in [x-1, x+1, x*2]:
                if 100000 >= i >= 0:
                    if not visited[i]:
                        visited[i] += visited[x] + 1
                        Q.append(i)


N, K = map(int, input().split())
print(bfs(N))