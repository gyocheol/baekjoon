import sys
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
sticker = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        r1, c1 = sticker[i]
        r2, c2 = sticker[j]
        if (r1+r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1+c2 <= w): # 둘다 회전하지 않았을 때
            ans = max(ans, r1 * c1 + r2 * c2)
        if (c1+c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1+r2 <= w): # 둘다 회전했을 때
            ans = max(ans, r1 * c1 + r2 * c2)
        if (c1+r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1+c2 <= w): # i 만 회전했을 때
            ans = max(ans, r1 * c1 + r2 * c2)
        if (r1+c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1+r2 <= w): # j 만 회전했을 때
            ans = max(ans, r1 * c1 + r2 * c2)
print(ans)