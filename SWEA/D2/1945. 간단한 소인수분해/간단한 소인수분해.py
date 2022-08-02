t = int(input())

for i in range(1, t+1):
    n = int(input())
    d = [2, 3, 5, 7, 11]
    cnt = [0, 0, 0, 0, 0]
    for j in range(len(d)):
        while True:
            if n % d[j] == 0:
                n = n // d[j]
                cnt[j] += 1
            else:
                break
    print(f"#{i} {' '.join(map(str, cnt))}")