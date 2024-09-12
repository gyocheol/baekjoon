n, k, m = map(int, input().split())
josephus = [i for i in range(1, n+1)]
switch = 0
idx = 0
flag = 0                                    # 우측 방향 0, 좌측 방향 1
ans = []
dirt = [k-1, -k]                            # 우측은 k-1 돌고 좌측은 -k만큼 돈다!
while josephus:
    l_j = len(josephus)
    if not switch % m and switch != 0:      # 제거 인원 충족 시 방향 변경
        flag = 0 if flag else 1
    idx = (idx+dirt[flag])%l_j
    ans.append(josephus.pop(idx))
    switch += 1
for i in range(n):
    print(ans[i])
