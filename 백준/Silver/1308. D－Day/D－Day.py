import datetime

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

day = int(str(datetime.date(y2,m2,d2) - datetime.date(y1,m1,d1)).split()[0])

over = 0
for i in range(1000):
    if not i % 400:
        over += 366
    elif not i % 100:
        over += 365
    elif not i % 4:
        over += 366
    else:
        over += 365

print(f"D-{day}" if over > day else "gg")