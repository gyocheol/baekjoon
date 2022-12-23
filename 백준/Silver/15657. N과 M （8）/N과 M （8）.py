def comb(n, r, k, s):
    if r == k:
        print(*t)
    else:
        for i in range(s, n):
            t[k] = arr[i]
            comb(n, r, k+1, i)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
t = [0] * M
comb(N, M, 0, 0)