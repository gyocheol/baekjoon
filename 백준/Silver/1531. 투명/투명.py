board = [[0] * 100 for _ in range(100)]
n, m = map(int, input().split())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a-1, c):
        for j in range(b-1, d):
            board[i][j] += 1
ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] > m:
            ans += 1
print(ans)