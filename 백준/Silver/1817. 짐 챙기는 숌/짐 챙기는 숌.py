n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    book = list(map(int, input().split()))
    box = 1
    total = 0
    for i in book:
        if total+i <= m:
            total += i
        else:
            box += 1
            total = i
    print(box)
