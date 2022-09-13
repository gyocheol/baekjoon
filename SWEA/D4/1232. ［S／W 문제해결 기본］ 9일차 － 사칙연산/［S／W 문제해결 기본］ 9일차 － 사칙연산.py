def post(node):
    if fc[node] == 0 or sc[node] == 0:
        return num[node]
    else:
        left = post(fc[node])
        right = post(sc[node])
        if op[node] == '-':
            num[node] = left - right
        elif op[node] == '+':
            num[node] = left + right
        elif op[node] == '*':
            num[node] = left * right
        elif op[node] == '/':
            num[node] = left // right
        return num[node]


for t in range(1, 11):
    N = int(input())
    op = [''] * (N + 1)
    fc, sc, num = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
    for i in range(N):
        temp = list(input().split())
        # print(temp)
        idx = int(temp[0])
        if len(temp) > 2:
            op[idx] = temp[1]
            fc[idx] = int(temp[2])
            sc[idx] = int(temp[3])
        else:
            num[idx] = int(temp[1])
    print(f'#{t} {post(1)}')
