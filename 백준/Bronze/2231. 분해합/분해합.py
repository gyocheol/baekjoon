N = int(input())
for i in range(1, N):
    str_N = str(i)
    total = 0
    for j in str_N:
        total += int(j)
    if not N - i - total:
        print(i)
        break
else:
    print(0)