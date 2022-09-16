
def bfs(x, y):
    l = []
    l.append((x, y))
    start = arr[x][y]
    cnt = 1
    while l:
        x, y = l.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[x][y] + 1 == arr[nx][ny]:
                    cnt += 1
                    l.append((nx, ny))
                    break
    return start, cnt


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t}', end=' ')
    s = []
    count = 0
    for i in range(N):
        for j in range(N):
            start, cnt = bfs(i, j)
            if cnt > count:
                count = cnt
                s = []
                s.append(start)
            elif cnt == count:
                s.append(start)
    print(min(s), count)