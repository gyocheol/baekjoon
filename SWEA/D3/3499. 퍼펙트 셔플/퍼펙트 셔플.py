T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = input().split()
    print(f'#{t}', end=' ')
    ans = []
    ans2 = ''
    a = []
    b = []
    if N % 2 == 0:
        a.append(arr[:N//2])
        b.append(arr[N//2:])
        for i in range(N//2):
            ans.append(a[0][i] + ' ' + b[0][i])

    else:
        a.append(arr[:N // 2+1])
        b.append(arr[N // 2+1:])
        for j in range(len(b[0])):
            ans2 += a[0][j] + ' ' + b[0][j] + ' '

    if N % 2 == 0:
        print(*ans)
    else:
        print(ans2 + a[0][-1])