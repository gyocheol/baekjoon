def solve(a):
    cnt = 0
    for i in range(N):
        stack = []
        for j in range(N):
            if a[i][j] == 1:
                stack.append(a[i][j])
            else:
                if len(stack) == K:
                    cnt += 1
                    stack = []
                else:
                    stack = []
        if len(stack) == K:
            cnt += 1

    return cnt

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    # 가로
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 세로
    arr2 = list(zip(*arr))
    # print(arr2)
    print(f'#{t} {solve(arr)+solve(arr2)}')