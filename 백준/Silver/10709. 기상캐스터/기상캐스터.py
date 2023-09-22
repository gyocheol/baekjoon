h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]
ans = [[0] * w for _ in range(h)]
for i in range(h):
    flag = False
    day = 0
    for j in range(w):
        if arr[i][j] == "c":
            day = 0
            flag = True
            ans[i][j] = day
        else:
            if flag:
                day += 1
                ans[i][j] = day
            else:
                ans[i][j] = -1
for i in range(h):
    print(*ans[i])