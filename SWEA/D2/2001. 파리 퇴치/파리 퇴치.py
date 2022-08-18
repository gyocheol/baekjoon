T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # x = [x for x in range(M)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for h in range(M):
                for k in range(M):
                    total += arr[i+h][j+k]
            if total > result:
                result = total
    print(result)