import sys
input = sys.stdin.readline


def dfs():
    if len(t) == M:
        print(*t)
        return
    num = 0
    for z in range(N):
        if not visited[z] and num != arr[z]:
            t.append(arr[z])
            visited[z] = True
            num = arr[z]
            dfs()
            t.pop()
            visited[z] = False


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False] * N
t = []

dfs()