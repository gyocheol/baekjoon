def solve(n, r, k, s):
    if r == k:
        print(*t)
    else:
        for i in range(s, n-r+k+1):
            t[k] = num[i]
            solve(n, r, k+1, i+1)


N, M = map(int, input().split())
num = [i for i in range(1, N+1)]
t = [0] * M
solve(N, M, 0, 0)