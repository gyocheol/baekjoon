from collections import deque
import sys
input = sys.stdin.readline


def dijkstra(x):
    Q = deque()
    Q.append((x, 0))
    D[x] = 0
    while Q:
        ss, cost = Q.popleft()
        if D[ss] < cost:
            continue

        for ee, cc in adj[ss]:
            if D[ee] > cost + cc:
                D[ee] = cost + cc
                Q.append((ee, cost + cc))



V = int(input())
E = int(input())
adj = [[] for _ in range(V+1)]
D = [10**10] * (V+1)

for _ in range(E):
    s, e, c = map(int, input().split())
    adj[s].append((e, c))

start, end = map(int, input().split())

dijkstra(start)
print(D[end])