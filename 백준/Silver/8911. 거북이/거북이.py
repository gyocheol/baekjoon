import sys
input = sys.stdin.readline

n = int(input())
dx = [1, 0, -1, 0]  # 시계방향
dy = [0, 1, 0, -1]
for _ in range(n):
    order = input().rstrip()
    total_x = [0]
    total_y = [0]
    idx = 0         # 시작은 북
    x, y = 0, 0
    for i in order:
        idx = idx%4
        if i == 'F':
            x += dx[idx]
            y += dy[idx]
            total_x.append(x)
            total_y.append(y)
        elif i == 'B':
            x -= dx[idx]
            y -= dy[idx]
            total_x.append(x)
            total_y.append(y)
        elif i == 'L':
            idx -= 1
        elif i == 'R':
            idx += 1

    print(abs(max(total_x)-min(total_x))*abs(max(total_y)-min(total_y)))
