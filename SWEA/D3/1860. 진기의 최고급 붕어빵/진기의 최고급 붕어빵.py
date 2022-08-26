def solve():
    bread = 0
    for time in range(11112):
        if time % M == 0 and time != 0:
            bread += K

        for a in arr:
            if a == time:
                if bread == 0:
                    return 'Impossible'
                bread -= 1
    return 'Possible'


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{t} {solve()}')