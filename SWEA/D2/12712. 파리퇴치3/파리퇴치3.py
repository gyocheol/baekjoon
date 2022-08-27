# 우좌하상
def solve(a):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ans = 0
    for i in range(N):
        for j in range(N):
            total = 0
            total += a[i][j]
            for x in range(4):
                for z in range(1, M):
                    if N > i+dx[x]*z >= 0 and N > j+dy[x]*z >= 0:
                        total += a[i+dx[x]*z][j+dy[x]*z]
                    else:
                        pass
            if total > ans:
                ans = total
    return ans

# 대각선
def solve2(a):
    dx = [1, -1, -1, 1]
    dy = [-1, -1, 1, 1]
    ans = 0
    for i in range(N):
        for j in range(N):
            total = 0
            total += a[i][j]
            for x in range(4):
                for z in range(1, M):
                    if N > i + dx[x] * z >= 0 and N > j + dy[x] * z >= 0:
                        total += a[i + dx[x] * z][j + dy[x] * z]
                    else:
                        pass
            if total > ans:
                ans = total
    return ans


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t}', end=' ')
    if solve(arr) > solve2(arr):
        print(solve(arr))
    else:
        print(solve2(arr))