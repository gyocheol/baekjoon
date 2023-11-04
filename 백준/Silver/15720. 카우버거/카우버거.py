b, s, c = map(int, input().split())
ans = [0, 0]

burger = sorted(list(map(int, input().split())), reverse=True)
side = sorted(list(map(int, input().split())), reverse=True)
coke = sorted(list(map(int, input().split())), reverse=True)

ans[0], ans[1] = sum(burger)+sum(side)+sum(coke), sum(burger)+sum(side)+sum(coke)
n = min(b, s, c)
ans[1] -= (sum(burger[:n]) + sum(side[:n]) + sum(coke[:n]))*0.1

for i in ans:
    print(int(i))