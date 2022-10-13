import sys
input = sys.stdin.readline


def solve(x):
    if x > 5:
        DP = [0, 1, 1, 1, 2, 2] + [0] * (N-5)
        for i in range(6, N+1):
            DP[i] = DP[i-1] + DP[i-5]
        return DP[x]
    else:
        DP = [0, 1, 1, 1, 2, 2]
        return DP[x]


for _ in range(int(input())):
    N = int(input())
    print(solve(N))