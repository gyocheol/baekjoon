t, n = map(int, input().split())
ranks = [""]*(n-3)
for _ in range(t):
    kayak = input()
    rank = 0
    for i in range(n-2, 0, -1):
        if kayak[i] == ".":
            rank += 1
        else:
            ranks[rank] += kayak[i]
            break
ans = {}
rank = 1
for i in ranks:
    if i:
        for j in i:
            ans[int(j)] = rank
        rank += 1

for i in range(1, 10):
    print(ans[i])