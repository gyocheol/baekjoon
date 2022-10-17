import sys; input = sys.stdin.readline;
from collections import deque

def bfs():
    while Q:
        start = Q.popleft()
        for s in tree[start]:
            if not parents[s]:
                parents[s] = start
                Q.append(s)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):                # 트리 구조 트리에 저장
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

Q = deque()
Q.append(1)
parents = [0] * (N+1)

bfs()
# print(parents)
ans = parents[2:]

for i in ans:
    print(i)