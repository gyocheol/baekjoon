N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

k = 2

for i in range(1, N):
    for j in range(k):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i-1][j]
        elif i == j:
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            arr[i][j] = max(arr[i-1][j-1] + arr[i][j], arr[i-1][j]+arr[i][j])
    k += 1

print(max(arr[N-1]))
