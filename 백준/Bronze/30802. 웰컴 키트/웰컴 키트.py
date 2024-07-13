n = int(input())
t_shirt = list(map(int, input().split()))
t,p = map(int,input().split())

ans = 0
for i in range(len(t_shirt)):
    if t_shirt[i]%t == 0:
        ans += int(t_shirt[i] / t)
    else:
        ans += (int(t_shirt[i] / t) + 1)

print(ans)
print(int(sum(t_shirt) / p), sum(t_shirt) % p)