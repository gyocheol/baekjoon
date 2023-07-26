import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, max(arr)
while s <= e:
    mid = (s + e) // 2
    total = 0
    for i in arr:
        if i > mid:
            total += i - mid
    if total >= m:
        s = mid + 1
    else:
        e = mid - 1
print(e)