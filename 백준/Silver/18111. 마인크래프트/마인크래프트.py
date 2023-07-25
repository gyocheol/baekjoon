import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_n = max(max(arr))
min_n = min(min(arr))
res = [10**10, 0]

for v in range(min_n, max_n+1):
    up, down, time = 0, 0, 0

    for i in range(n):
        for j in range(m):
            diff = arr[i][j] - v
            if diff > 0:
                down += diff
            else:
                up -= diff

    if down + b >= up:
        time = down * 2 + up
        if res[0] >= time:
            res[0] = time
            res[1] = v

print(*res)
