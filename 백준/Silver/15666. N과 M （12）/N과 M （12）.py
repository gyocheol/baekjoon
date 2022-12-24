def comb(r, k, s):
    if r == k:
        print(*t)
    else:
        for i in range(s, n):
            t[k] = arr[i]
            comb(r, k+1, i)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))
t = [0] * M
n = len(arr)
comb(M, 0, 0)