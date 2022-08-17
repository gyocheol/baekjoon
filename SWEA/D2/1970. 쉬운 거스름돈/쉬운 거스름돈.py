money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]   # 돈 8종류

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t}')
    change = [0] * len(money)

    for i in range(len(money)):
        while N - money[i] >= 0:
            change[i] += 1
            N -= money[i]
    print(*change)