def dfs():
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        if arr[i] not in result:
            result.append(arr[i])
            dfs()
            result.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
dfs()