T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    arr = list(map(int, input()))
    # print(arr)
    N = len(arr)
    c = [0] * N
    cnt = 0
    for i in range(N):
        if c == arr:
            break

        if c[i] != arr[i]:
            if c[i] == 0:
                for j in range(i, N):
                    c[j] = 1
            else:
                for j in range(i, N):
                    c[j] = 0
            cnt += 1
    print(cnt)