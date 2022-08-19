T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f"#{t}", end=' ')
    n = [2, 3, 5, 7, 11]
    cnt = [0] * len(n)
    for i in range(len(n)):
        while True:
            if N % n[i] == 0:
                N = N // n[i]
                cnt[i] += 1
            else:
                break
    print(*cnt)