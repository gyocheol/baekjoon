def post(node):
    if node:
        post(fc[node])
        print(oper[node], end='')
        post(sc[node])

T = 10
for t in range(1, T+1):
    N = int(input())
    print(f'#{t}', end=' ')
    oper = [''] * (N+1)
    fc, sc = [0]*(N+1), [0]*(N+1)
    for _ in range(N):
        temp = list(input().split())
        # print(temp)
        idx = int(temp[0])
        if len(temp) == 4:
            oper[idx] = temp[1]
            fc[idx] = int(temp[2])
            sc[idx] = int(temp[3])
        elif len(temp) == 3:
            oper[idx] = temp[1]
            fc[idx] = int(temp[2])
        else:
            oper[idx] = temp[1]
    post(1)
    print()