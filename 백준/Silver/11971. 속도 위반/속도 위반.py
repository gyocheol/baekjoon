n, m = map(int, input().split())
drive = [0] * 101

km = 1
for i in range(n):
    k, s = map(int, input().split())
    for j in range(km, km+k):
        drive[j] = s
    km += k

km2 = 1
for i in range(m):
    k, s = map(int, input().split())
    for j in range(km2, km2+k):
        drive[j] = s - drive[j]
    km2 += k

print(max(drive))