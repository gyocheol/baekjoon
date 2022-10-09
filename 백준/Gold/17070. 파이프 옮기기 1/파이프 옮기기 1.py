n = int(input())
# n = 3
graph = [list(map(int, input().split())) for _ in range(n)]
# 가로, 세로, 대각선 = 3
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
# 파이프의 초기 위치
dp[0][0][1] = 1
# print(dp)

# 처음에 가로로 갈 수 있는 곳에 파이프를 이동
for i in range(2, n):
    if not graph[0][i]:
        dp[0][0][i] = dp[0][0][i-1]
# print(dp)

# 파이프 이동
for i in range(1, n):
    for j in range(2, n):

        # 파이프가 대각선으로 이동 가능 한 경우
        if not graph[i][j] and not graph[i-1][j] and not graph[i][j-1]:
            dp[2][i][j] = sum(dp[k][i-1][j-1] for k in range(3))
# print(dp)

        # 파이프가 가로/세로로 이동 가능한 경우
        if not graph[i][j]:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]     # 가로
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]     # 세로
# print(dp)
print(sum(dp[k][-1][-1] for k in range(3)))