n = int(input())
arr = [list(input()) for _ in range(n)]

r = c = 0
for i in range(n):
    total_r = total_c = 0
    for j in range(n):
        if arr[i][j] == ".":
            total_r += 1
        else:
            total_r = 0
        if arr[j][i] == ".":
            total_c += 1
        else:
            total_c = 0

        if total_r == 2:
            r += 1
        if total_c == 2:
            c += 1

print(r, c)
