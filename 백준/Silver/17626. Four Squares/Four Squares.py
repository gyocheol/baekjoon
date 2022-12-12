import math
import sys
input = sys.stdin.readline

N = int(input())
dp = [10**10] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    for j in range(int(math.sqrt(i)), 0, -1):
        dp[i] = min(dp[i], 1 + dp[i-j**2])
print(dp[-1])