def dfs(x, y, n):
    if n == 1:
        print(arr[x][y], end='')
        return
    num = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            # 처음에 2차원 배열 전체가 같은지 판단
            # 아니라면 아래로 내려감
            if num != arr[i][j]:
                print('(', end='')
                n //= 2
                # 4등분
                dfs(x, y, n)
                # 4등분의 4등분
                dfs(x, y+n, n)
                # 4등분의 4등분
                dfs(x+n, y, n)
                # 4등분의 4등분의 4등분
                dfs(x+n, y+n, n)
                print(')', end='')
                return

    print(arr[x][y], end='')
    return


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

dfs(0, 0, N)