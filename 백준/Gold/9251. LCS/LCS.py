import sys
input = sys.stdin.readline

a = " " + input().rstrip()
b = " " + input().rstrip()
la, lb = len(a), len(b)

dp = [[0] * lb for _ in range(la)]

for i in range(1, la):
    for j in range(1, lb):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])