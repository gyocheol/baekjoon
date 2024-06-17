T = int(input())
for t in range(T):
    n = int(input())
    ans = []
    values = list(map(int, input().split()))
    while values:
        temp = values.pop(0)
        if int(temp//0.75) in values:
            ans.append(str(temp))
            values.remove(int(temp//0.75))

    print(f'Case #{t+1}: {" ".join(ans)}')
