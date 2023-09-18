n, m = map(int, input().split())
apples = [int(input()) for i in range(int(input()))]
now = 1
ans = 0
for i in apples:
    if i in [i for i in range(now, now+m)]:
        pass
    else:
        move = now
        min_num = 10
        for j in range(i-m+1, i+1):
            if min_num > abs(j-move):
                min_num = abs(j-move)
                now = j
        ans += abs(now - move)
print(ans)