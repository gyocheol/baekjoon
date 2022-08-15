def benefit(arr, n):
    if n > 0:
        return sum(arr[n:-n])
    elif n == 0:
        return sum(arr)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(f'#{t}', end=' ')
    ans = 0
    i = [i for i in range(N//2+1)]
    j = [j for j in range(N//2, -1, -1)]
    for h in range(N//2+1):
        ans += benefit(arr[i[h]], j[h])

    for h in range(N//2+1, N):
        ans += benefit(arr[h], h-(N//2))
    print(ans)