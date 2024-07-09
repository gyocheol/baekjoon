n, m, d = map(int, input().split())
arr = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        flag = True
        if arr[i][j] == ".":
            if j <= m-d:
                if not arr[i][j:j+d].count("#"):
                    ans += 1
            if i <= n-d:
                for k in range(d):
                    if arr[i+k][j] == "#":
                        flag = False
                        break
                if flag:
                    ans += 1

print(ans)