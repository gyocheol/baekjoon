import sys
input = sys.stdin.readline

def compare(arr):
    max_cnt = 1
    for x in range(n):
        col_total = 1
        row_total = 1
        for y in range(1, n):
            if arr[x][y] == arr[x][y-1]:
                col_total += 1
            else:
                col_total = 1
            max_cnt = max(col_total, max_cnt)

            if arr[y][x] == arr[y-1][x]:
                row_total += 1
            else:
                row_total = 1
            max_cnt = max(col_total, max_cnt)
            max_cnt = max(row_total, max_cnt)

    return max_cnt


n = int(input())
board = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
            cnt = compare(board)
            ans = max(ans, cnt)
            board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
        if i + 1 < n:
            board[i-1][j], board[i][j] = board[i][j], board[i-1][j]
            cnt = compare(board)
            ans = max(ans, cnt)
            board[i-1][j], board[i][j] = board[i][j], board[i-1][j]
    if ans == n:
        break

print(ans)