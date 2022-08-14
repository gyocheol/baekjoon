T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t}')
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i > 0 and j > 0:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            elif j == 0:
                arr[i][j] = 1

    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()