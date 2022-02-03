r = 0
num = 0

for _ in range(10):
    a, b = map(int, input().split())
    num -= a
    num += b
    r = max(r, num)

print(r)