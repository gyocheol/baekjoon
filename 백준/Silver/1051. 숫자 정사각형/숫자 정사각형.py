n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

ans = 1
for i in range(n):
    for j in range(m):
        total = 0
        for k in range(min(n-i, m-j)):
                if arr[i][j] == arr[i+k][j] and arr[i][j] == arr[i+k][j+k] and arr[i][j] == arr[i][j+k]:
                    total += 1
                    if total > ans:
                        ans = total
                else:
                    total += 1

print(ans**2)

