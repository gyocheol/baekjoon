def rotation(a):
    lst = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            lst[i][j] = a[N-j-1][i]
    return lst

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t}')
    r90 = rotation(arr)
    r180 = rotation(r90)
    r270 = rotation(r180)
    for i in range(N):
        print(''.join(map(str, r90[i])), end=' ')
        print(''.join(map(str, r180[i])), end=' ')
        print(''.join(map(str, r270[i])))