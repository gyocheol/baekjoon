import heapq

def dijkstra(s):
    D[s] = 0
    q = [(0, start)]
    while q:
        w, cur = heapq.heappop(q)
        if D[cur] < w:
            continue

        for d, ww in adj[cur]:
            cost = D[cur] + ww
            if D[d] > cost:
                D[d] = cost
                heapq.heappush(q, (cost, d))


V = int(input())
E = int(input())
adj = [[] for _ in range(V+1)]
D = [10**10] * (V+1)

for i in range(E):
    s, e, d = map(int, input().split())
    adj[s].append((e, d))

start, end = map(int, input().split())

# print(adj)
dijkstra(start)
print(D[end])