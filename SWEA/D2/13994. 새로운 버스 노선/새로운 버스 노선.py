T = int(input())
for t in range(1, T+1):
    N = int(input())
    c = [0] * 1000000
    for _ in range(N):
        kind, A, B = map(int, input().split())
        # if A > B:
        #     A, B = B, A
        if kind == 1:
            for i in range(A, B+1):
                c[i] += 1
        elif kind == 2:
            for i in range(A, B+1, 2):
                c[i] += 1

        elif kind == 3:
            for i in range(A, B+1):
                if A % 2 == 0:
                    if i % 4 == 0:
                        c[i] += 1
                    else:
                        pass
                else:
                    if i % 3 == 0 and i % 10 != 0:
                        c[i] += 1
                    else:
                        pass
    print(f'#{t} {max(c)}')