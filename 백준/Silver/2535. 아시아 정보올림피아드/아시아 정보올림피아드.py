n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [0] * (arr[-1][0] + 1)
arr.sort(key=lambda x : x[2], reverse=True)

ans = []
for g, s, b in arr:
    if not check[g]:
        check[g] = 1
        ans.append([g, s])
    else:
        if check[g] == 2:
            pass
        else:
            check[g] += 1
            ans.append([g, s])
    if len(ans) == 3:
        break
for i in ans:
    print(*i)