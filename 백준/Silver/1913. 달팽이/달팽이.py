import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
board = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

r = c = n//2
ans = [r+1, c+1] if m == 1 else []
num = 1
flag = 0
board[r][c] = num

while True:
    for i in range(4):
        for _ in range(flag):
            r += dx[i]
            c += dy[i]
            num += 1
            board[r][c] = num
            if num == m:
                ans = [r+1, c+1]
    if r == c == 0:
        break
    r -= 1
    c -= 1
    flag += 2

for i in range(n):
    print(*board[i])
print(*ans)