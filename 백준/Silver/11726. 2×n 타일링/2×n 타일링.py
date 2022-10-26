import sys
input = sys.stdin.readline

dp = [0]
dp.append(1)
dp.append(2)
for i in range(3, 1001):
    dp.append(dp[i-1]+dp[i-2])
ans = dp[int(input())]
if ans < 10007:
    print(ans)
else:
    print(ans % 10007)