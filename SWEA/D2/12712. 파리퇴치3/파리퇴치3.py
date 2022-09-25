def solve1():
    ans = 0
    for i in range(N):
        for j in range(N):
            total = arr[i][j]
            for k in range(1, M):
                for z in range(4):
                    ii = i + di[z] * k
                    jj = j + dj[z] * k
                    if 0 <= ii < N and 0 <= jj < N:
                        total += arr[ii][jj]
            if total > ans:
                ans = total
    return ans


def solve2():
    ans = 0
    for x in range(N):
        for y in range(N):
            total = arr[x][y]
            for k in range(1, M):
                for z in range(4):
                    xx = x + dx[z] * k
                    yy = y + dy[z] * k
                    if 0 <= xx < N and 0 <= yy < N:
                        total += arr[xx][yy]
            if total > ans:
                ans = total
    return ans


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
dx = [-1, 1, -1, 1]
dy = [-1, -1, 1, 1]

for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1}', end=' ')
    # print(arr)
    if solve1() > solve2():
        print(solve1())
    else:
        print(solve2())