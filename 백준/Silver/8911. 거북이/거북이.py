import sys
input = sys.stdin.readline

n = int(input())
dx = [1, 0, -1, 0]  # 시계방향
dy = [0, 1, 0, -1]
for _ in range(n):
    order = input().rstrip()
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    idx = 0         # 시작은 북
    x, y = 0, 0
    for i in order:
        idx = idx%4
        if i == 'F':
            x += dx[idx]
            y += dy[idx]
        elif i == 'B':
            x -= dx[idx]
            y -= dy[idx]
        elif i == 'L':
            idx -= 1
        elif i == 'R':
            idx += 1
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
    print(abs(max_x-min_x)*abs(max_y-min_y))
