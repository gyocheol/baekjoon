import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    total = ans % (a+b)
    if total < b:
        ans += b-total
    ans += 1
print(ans)
