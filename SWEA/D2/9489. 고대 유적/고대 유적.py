def solve1():
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if ans < cnt:
                    ans = cnt
                cnt = 0
        if ans < cnt:
            ans = cnt
    return ans


def solve2():
    ans = 0
    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if ans < cnt:
                    ans = cnt
                cnt = 0
        if ans < cnt:
            ans = cnt
    return ans


for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1}', end=' ')
    if solve1() > solve2():
        print(solve1())
    else:
        print(solve2())