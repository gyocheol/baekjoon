def dfs(x, y, n):
    num = arr[x][y]
    if n == 1:
        num_list.append(arr[x][y])
        return

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != arr[i][j]:
                n //= 3
                dfs(x, y, n)
                dfs(x+n, y, n)
                dfs(x+n*2, y, n)
                dfs(x, y+n, n)
                dfs(x, y+n*2, n)
                dfs(x+n, y+n, n)
                dfs(x+n*2, y+n, n)
                dfs(x+n, y+n*2, n)
                dfs(x+n*2, y+n*2, n)
                return

    num_list.append(arr[x][y])
    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
num_list = []

dfs(0, 0, N)
# print(num_list)
print(num_list.count(-1))
print(num_list.count(0))
print(num_list.count(1))