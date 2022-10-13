import sys
input = sys.stdin.readline

dp = [0] * 1000001
N = int(input())
dp[1], dp[2] = 1, 2
for i in range(3, N+1):
    if dp[i-2] + dp[i-1] >= 15746:
        dp[i] = (dp[i-2] + dp[i-1]) % 15746
    else:
        dp[i] = dp[i - 2] + dp[i - 1]
print(dp[N])