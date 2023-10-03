import sys
input = sys.stdin.readline

n, d = map(int, input().split())
arr = [i for i in range(1, n+1)]
ans = 0
for num in arr:
    for i in str(num):
        if int(i) == d:
            ans += 1

print(ans)