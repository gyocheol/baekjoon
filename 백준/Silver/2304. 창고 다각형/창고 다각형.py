n = int(input())
max_val = 0
idx = 0
warehouse = [0] * 1001      # 0이상 1000이하
for _ in range(n):
    l, h = map(int, input().split())
    warehouse[l] = h
    if h > max_val:
        max_val = h
        idx = l
ans = 0
total = 0
for i in range(idx+1):          # 왼쪽 그룹(최대 값 포함)
    total = max(warehouse[i], total)
    ans += total
total = 0
for i in range(1000, idx, -1):  # 오른쪽 그룹
    total = max(warehouse[i], total)
    ans += total
print(ans)

