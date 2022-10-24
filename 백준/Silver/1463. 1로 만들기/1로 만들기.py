dp = [0] * 1000001
N = int(input())
if not dp[N]:
    for i in range(2, N+1):
        dp[i] = dp[i-1]+1
        if not i % 3:
            dp[i] = min(dp[i], dp[i//3]+1)
        if not i % 2:
            dp[i] = min(dp[i], dp[i//2]+1)
    print(dp[N])
else:
    print(dp[N])