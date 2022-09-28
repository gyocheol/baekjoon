import sys
input = sys.stdin.readline

def dfs(x):
    global cnt
    visited[x] = True
    for y in adj[x]:
        if visited[y]: continue
        cnt += 1
        dfs(y)

# 인자리스트 받는 형식

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]      # 인자리스트
cnt = 0
visited = [False] * (N+1)           # 1 ~ N 까지 이므로 (N+1) 을 곱해줌
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
dfs(1)
print(cnt)