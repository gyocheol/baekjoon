N = int(input())
for i in range(max(1, N-9*len(str(N))), N):
    str_N = str(i)
    total = 0
    for j in str_N:
        total += int(j)
    if not N - i - total:
        print(i)
        break
else:
    print(0)