arr = [True] * 10001
for i in range(1, 10000):
    x = str(i)
    total = 0
    for j in x:
        total += int(j)
    if i + total < 10001:
        arr[i+total] = False

for i in range(1, 10001):
    if arr[i]:
        print(i)