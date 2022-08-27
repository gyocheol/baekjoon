# 가로
def solve(a):
    ans = 0
    for i in range(N):
        total = 0
        for j in range(M):
            if a[i][j]:
                total += a[i][j]

            elif a[i][j] == 0:
                if total > ans:
                    ans = total
                    total = 0

        if total > ans:
            ans = total
    return ans


# 세로
def solve2(a):
    ans = 0
    for i in range(M):
        total = 0
        for j in range(N):
            if a[j][i]:
                total += a[j][i]

            elif a[j][i] == 0:
                if total > ans:
                    ans = total
                    total = 0
        if total > ans:
            ans = total
    return ans


T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    if solve(arr) > solve2(arr):
        print(solve(arr))
    else:
        print(solve2(arr))