dp = [[0] * 14 for _ in range(15)]
dp[0][0], dp[1][0] = 1, 1
for i in range(1, 14):
    dp[0][i] = dp[0][i-1] + 1
    dp[i+1][0] = 1

for i in range(1, 15):
    for j in range(1, 14):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])