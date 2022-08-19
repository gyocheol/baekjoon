def solve(n):
    stack = []
    cnt = 0
    i = 0
    n.append(' ')
    while len(n)-1 > i:
        if n[i] == '(':
            stack.append(n[i])
            if n[i+1] == ')':
                if len(stack) > 0:
                    stack.pop()
                    cnt += len(stack)
                    i += 2
            else:
                i += 1

        elif n[i] == ')':
            if len(stack) > 0:
                stack.pop()
                cnt += 1
                i += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    N = list(input())
    print(f'#{t}', end=' ')
    print(solve(N))