'''
# 시간초과..ㅜ
from collections import deque
import sys
input = sys.stdin.readline
# import time
# starttime = time.time()

def f(n):
    while Q:
        x = Q.popleft()
        if x == 0:
            ans[0] += 1
        elif x == 1:
            ans[1] += 1
        if x-1 >= 1 or x-2 >= 1 or x-2 >= 0:
            Q.append(x-1)
            Q.append(x-2)

N = int(input())
for _ in range(N):
    ans = [0, 0]
    x = int(input())
    Q = deque()
    Q.append(x)
    f(x)
    print(*ans)

# print(time.time()-starttime)
'''

dp = [[] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]
dp[3] = [1, 2]
for i in range(4, 41):
    dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]

N = int(input())
for _ in range(N):
    n = int(input())
    print(*dp[n])