n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
n2, m2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(n2)]

for i in range(n):
    total = [0] * m2
    for j in range(m):
        for k in range(m2):
            total[k] += A[i][j]*B[j][k]
    print(*total)