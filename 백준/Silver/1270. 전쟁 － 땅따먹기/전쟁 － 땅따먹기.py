import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    grounds = {}
    ground = input().split()
    for g in ground:
        try: grounds[g] += 1
        except: grounds[g] = 1
    flag = True
    len_ground = len(ground)
    win = len_ground // 2 + 1 if len_ground % 2 else len_ground // 2
    for k, v in grounds.items():
        if v >= win:
            print(k)
            flag = False
            break
    if flag:
        print("SYJKGW")


''' 메모리 초과
set_armies = []
for i in range(n):
    ground = input().split()
    grounds.append(ground)
    set_armies.append(set(ground))

ans = []
for i in range(n):
    len_ground = len(grounds[i])
    win = len_ground//2+1 if len_ground%2 else len_ground//2
    total = []
    for army_num in set_armies[i]:
        if grounds[i].count(army_num) >= win:
            total.append(army_num)
    if total:
        ans.append(total[0])
    else:
        ans.append("SYJKGW")
for i in range(n):
    print(ans[i])
'''

