n = int(input())
p = list(map(int, input().split()))
ans = 0
a_total = 1
for a in range(n-3):
    a_total *= p[a]
    b_total = 1
    for b in range(a+1, n-2):
        b_total *= p[b]
        c_total = 1
        for c in range(b+1, n-1):
            c_total *= p[c]
            d_total = 1
            for d in range(c+1, n):
                d_total *= p[d]
            ans = max(ans, a_total+b_total+c_total+d_total)
print(ans)