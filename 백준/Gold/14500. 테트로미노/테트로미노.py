# 직선
def solve1(x, y):
    global ans
    total1, total2 = 0, 0
    for k in range(4):
        if 0 <= x + 1 * k < N:
            total2 += arr[x + 1 * k][y]
        if 0 <= y + 1 * k < M:
            total1 += arr[x][y + 1 * k]
    if total1 > ans:
        ans = total1
    if total2 > ans:
        ans = total2


# 정사각형
def solve2(x, y):
    global ans
    total = 0
    if 0 <= x + 1 < N and 0 <= y + 1 < M:
        total = arr[x][y] + arr[x+1][y] + arr[x][y+1] + arr[x+1][y+1]
    if total > ans:
        ans = total


# ㄴ
def solve3(x, y):
    global ans
    total1, total2, total3, total4 = 0, 0, 0, 0
    total5, total6, total7, total8 = 0, 0, 0, 0
    total9, total10, total11, total12 = 0, 0, 0, 0
    for k in range(3):
        # 아래로
        if 0 <= x + 1 * k < N:
            total1 += arr[x + 1 * k][y]
            total2 += arr[x + 1 * k][y]
            total3 += arr[x + 1 * k][y]
            total4 += arr[x + 1 * k][y]
            total9 += arr[x + 1 * k][y]
            total10 += arr[x + 1 * k][y]
        # 오른쪽으로
        if 0 <= y + 1 * k < M:
            total5 += arr[x][y + 1 * k]
            total6 += arr[x][y + 1 * k]
            total7 += arr[x][y + 1 * k]
            total8 += arr[x][y + 1 * k]
            total11 += arr[x][y + 1 * k]
            total12 += arr[x][y + 1 * k]

    if 0 <= x+2 < N and 0 <= y+1 < M:
        total1 += arr[x+2][y+1]
    if 0 <= x+2 < N and 0 <= y-1 < M:
        total2 += arr[x+2][y-1]
    if 0 <= y+1 < M:
        total3 += arr[x][y+1]
    if 0 <= y-1 < M:
        total4 += arr[x][y-1]
    if 0 <= x+1 < N and 0 <= y+2 < M:
        total5 += arr[x+1][y+2]
    if 0 <= x-1 < N and 0 <= y+2 < M:
        total6 += arr[x-1][y+2]
    if 0 <= x+1 < N:
        total7 += arr[x+1][y]
    if 0 <= x-1 < N:
        total8 += arr[x-1][y]
    if 0 <= x+1 < N and 0 <= y-1 < M:
        total9 += arr[x+1][y-1]
    if 0 <= x+1 < N and 0 <= y+1 < M:
        total10 += arr[x+1][y+1]
    if 0 <= x+1 < N and 0 <= y+1 < M:
        total11 += arr[x+1][y+1]
    if 0 <= x-1 < N and 0 <= y+1 < M:
        total12 += arr[x-1][y+1]

    if max(total1, total2, total3, total4, total5, total6, total7, total8, total9, total10, total11, total12) > ans:
        ans = max(total1, total2, total3, total4, total5, total6, total7, total8, total9, total10, total11, total12)


def solve4(x, y):
    global ans
    total1, total2, total3, total4 = 0, 0, 0, 0
    if 0 <= x+2 < N and 0 <= y+1 < M:
        total1 = arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x+2][y+1]
    if 0 <= x+2 < N and 0 <= y-1 < M:
        total2 = arr[x][y] + arr[x+1][y] + arr[x+1][y-1] + arr[x+2][y-1]
    if 0 <= x+1 < N and 0 <= y+2 < M:
        total3 = arr[x][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+1][y+2]
    if 0 <= x-1 < N and 0 <= y+2 < M:
        total4 = arr[x][y] + arr[x][y+1] + arr[x-1][y+1] + arr[x-1][y+2]

    if max(total1, total2, total3, total4) > ans:
        ans = max(total1, total2, total3, total4)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for j in range(M):
    for i in range(N):
        solve1(i, j)
        solve2(i, j)
        solve3(i, j)
        solve4(i, j)

print(ans)