import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    while x <= M * N:
        if not (x - y) % N:
            print(x)
            break
        else:
            x += M
    else:
        print(-1)