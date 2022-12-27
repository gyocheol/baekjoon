import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        DP[i+1][j+1] = DP[i][j+1] + DP[i+1][j] - DP[i][j] + arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1])