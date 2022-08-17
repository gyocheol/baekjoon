def cnt(a):
    c = 0
    for i in range(N):
        n = 0
        for j in range(N):
            if a[j][i] == 1:
                n = 1
            elif a[j][i] == 2 and n == 1:
                c += 1
                n = 0
    return c


T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{t}', end=' ')
    print(cnt(arr))