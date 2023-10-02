j = list(map(int, input().split()))
g = list(map(int, input().split()))

j_cnt = g_cnt = flag = 0
for i in range(9):
    j_cnt += j[i]
    if j_cnt > g_cnt:
        flag = 1
    g_cnt += g[i]

if flag:
    print("Yes")
else:
    print("No")