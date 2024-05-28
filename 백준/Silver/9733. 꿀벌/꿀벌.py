import sys

work = {}
orders = ["Re", "Pt", "Cc", "Ea", "Tb", "Cm", "Ex"]
cnt = 0
for i in orders:
    work[i] = 0
lines = sys.stdin.readlines()
for line in lines:
    order = list(line.split())
    for o in order:
        if o in work:
            work[o] += 1
        cnt += 1

for i in range(7):
    print(f'{orders[i]} {work[orders[i]]} {work[orders[i]] / cnt:.2f}')
print(f'Total {cnt} 1.00')