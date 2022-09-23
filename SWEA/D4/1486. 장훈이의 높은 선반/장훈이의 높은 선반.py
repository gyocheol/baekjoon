def comb(n, r, k, s):
    global ans
    if ans < sum(t) - B:
        return
    if k == r:
        if 0 <= sum(t) - B < ans:
            ans = sum(t) - B
        return
    else:
        for i in range(s, n-r+1+k):
            t[k] = arr[i]
            comb(n, r, k+1, i+1)


for t in range(int(input())):
    print(f'#{t+1}', end=' ')
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = 10**10
    for i in range(1, N+1):
        R = i
        t = [0] * R
        comb(N, R, 0, 0)
    print(ans)