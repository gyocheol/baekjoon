def solve(a):
    stack = []
    for i in range(int(N)):
        if len(stack) == 0:
            stack.append(a[i])
        else:
            if stack[-1] == a[i]:
                stack.pop()
            else:
                stack.append(a[i])
    return stack


T = 10
for t in range(1, T+1):
    N, arr = map(str, input().split())
    # print(arr)
    print(f'#{t} {"".join(solve(arr))}')