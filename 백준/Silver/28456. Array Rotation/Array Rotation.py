n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(int(input())):
    order = list(input().split())
    if order[0] == "1":
        r = int(order[1])-1
        arr[r] = [arr[r][-1]] + arr[r][:-1]
    else:
        A = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                A[j][n-i-1] = arr[i][j]
        arr = A
for i in range(n):
    print(*arr[i])
