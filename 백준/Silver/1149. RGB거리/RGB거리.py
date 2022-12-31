N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    for j in range(3):
        if i == 0:
            dp[i][j] = arr[i][j]
        elif j == 0:
            dp[i][j] = min(arr[i][j] + dp[i-1][j+1], arr[i][j] + dp[i-1][j+2])
        elif j == 1:
            dp[i][j] = min(arr[i][j] + dp[i - 1][j - 1], arr[i][j] + dp[i - 1][j + 1])
        elif j == 2:
            dp[i][j] = min(arr[i][j] + dp[i - 1][j - 1], arr[i][j] + dp[i - 1][j -2])

# print(dp)
print(min(dp[N-1]))