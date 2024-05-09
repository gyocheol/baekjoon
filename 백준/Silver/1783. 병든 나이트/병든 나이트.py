import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 0

if n == 1:
    ans = 1
elif n == 2:
    ans = min(4, (m+1)//2)
elif m < 7:
    ans = min(4, m)
else:
    ans = m-2

print(ans)