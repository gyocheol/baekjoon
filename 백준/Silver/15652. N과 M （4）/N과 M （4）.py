def comb(n, r, k, s):
    if r == k:
        print(*t)
    else:
        for i in range(s, n):
            t[k] = num[i]
            comb(n, r, k+1, i)


N, M = map(int, input().split())
num = [i for i in range(1, N+1)]
t = [0] * M
comb(N, M, 0, 0)
