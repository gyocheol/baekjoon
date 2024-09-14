k = int(input())

row = []
col = []
r_c = []
flag = False
for _ in range(6):
    x, y = map(int, input().split())
    if x < 3:
        col.append(y)
    else:
        row.append(y)
    r_c.append(y)
max_r = max(row)
max_c = max(col)
min_r = r_c[r_c.index(max_c) - 3]
min_c = r_c[r_c.index(max_r) - 3]
print((max_r * max_c - min_r * min_c)*k)
