N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr = arr[0:x-1] + arr[x-1:y][::-1] + arr[y:]
print(*arr)
