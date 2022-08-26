
T = int(input())
for t in range(1, T+1):
    N = int(input())
    c = [0] * 200
    print(f'#{t}', end=' ')
    for i in range(N):
        x1, y1 = map(int, input().split())
        x = (x1-1)//2
        y = (y1-1)//2
        if x < y:
            for j in range(x, y+1):
                c[j] += 1
        else:
            for j in range(y, x+1):
                c[j] += 1

    print(max(c))