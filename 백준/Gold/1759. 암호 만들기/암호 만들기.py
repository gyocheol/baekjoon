import sys
# sys.stdin = open('test_data/1759.txt')
input = sys.stdin.readline

def comb(n, r, k, s, p):
    if k == r:
        
        cnt = 0
        for i in p:
            if i in ['a', 'e', 'i', 'o', 'u']:
                cnt += 1
        if cnt and L-cnt >= 2:
            ans = ''.join(p)
            print(ans)

    else:
        for i in range(s, n-r+k+1):
            # t[k] = pw[i]
            # p.append(pw[i])
            comb(n, r, k+1, i+1, p+pw[i])

L, C = map(int, input().split())
arr = list(input().split())
# print(arr)
pw = []
for i in range(C):
    pw.append(arr[i])
# t = [0] * L
# p = []
pw.sort()
comb(C, L, 0, 0, '')