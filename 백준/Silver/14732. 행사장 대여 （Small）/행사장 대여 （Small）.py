import sys
input = sys.stdin.readline

n = int(input())
ans = 0
max_x, max_y = 0, 0
min_x, min_y = 500, 500
block = [[False] * 501 for _ in range(501)]
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    min_x = min(min_x, x1)
    min_y = min(min_y, y1)
    max_x = max(max_x, x2)
    max_y = max(max_y, y2)
    for r in range(x1, x2):
        for c in range(y1, y2):
            block[c][r] = True
            
for i in range(min_x, max_x):
    for j in range(min_y, max_y):
        if block[j][i]:
            ans += 1
print(ans)