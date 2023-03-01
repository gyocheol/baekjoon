N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    xx = arr[x-1]
    yy = arr[y-1]
    arr[y-1] = xx
    arr[x-1] = yy
print(*arr)