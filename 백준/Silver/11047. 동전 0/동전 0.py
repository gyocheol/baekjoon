N, K = map(int, input().split())
l = sorted([int(input()) for _ in range(N)], reverse=True)
cnt = 0
ans = K

for i in range(N):
    while ans >= l[i]:
        if ans-l[i] >= 0:
            ans = ans-l[i]
            cnt += 1
        if ans == 0:
            break
    if ans == 0:
        break
print(cnt)