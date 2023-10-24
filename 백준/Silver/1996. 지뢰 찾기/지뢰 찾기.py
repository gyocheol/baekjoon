def solution(num, x, y):
    for k in range(8):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0 <= nx < n and 0 <= ny < n and ans[nx][ny] != "*" and ans[nx][ny] != "M":
            if ans[nx][ny] == "":
                ans[nx][ny] = str(num)
            else:
                total = str(int(ans[nx][ny]) + num)
                if int(total) >= 10:
                    ans[nx][ny] = "M"
                else:
                    ans[nx][ny] = total


dx = [0, 0, 1, -1, -1, 1, 1, -1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]
n = int(input())
ans = [["0"] * n for _ in range(n)]
for i in range(n):
    mine = input()
    for j in range(len(mine)):
        if mine[j] != ".":
            ans[i][j] = "*"
            solution(int(mine[j]), i, j)

for i in range(n):
    print("".join(ans[i]))
