import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    DP = [0] * 101
    DP[1] = DP[2] = DP[3] = 1
    DP[4] = DP[5] = 2
    for i in range(6, N+1):
        DP[i] = DP[i-1] + DP[i-5]
    print(DP[N])