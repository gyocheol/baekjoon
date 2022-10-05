N = int(input())
city = list(map(int, input().split())) + [0]
oil = list(map(int, input().split()))

ans = 0
min_v = oil[0]

for i in range(N):
    if min_v >= oil[i]:
        min_v = oil[i]
        ans += min_v * city[i]
    else:
        ans += min_v * city[i]
print(ans)