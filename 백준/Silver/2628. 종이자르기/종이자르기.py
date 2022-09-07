c, r = map(int, input().split())
N = int(input())
col = [0, c]
row = [0, r]
for _ in range(N):
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        row.append(arr[1])
    else:
        col.append(arr[1])
col.sort()
row.sort()
col_l = []
row_l = []
for i in range(len(col)-1):
    col_l.append(col[i+1] - col[i])
for i in range(len(row)-1):
    row_l.append(row[i+1] - row[i])
print(max(col_l) * max(row_l))