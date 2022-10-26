import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

total = 0
dp = [0]

for i in arr:
    total += i
    dp.append(total)

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[e] - dp[s-1])
