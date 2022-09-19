N, M = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        ans[i][j] = arr1[i][j] + arr2[i][j]

for i in range(len(ans)):
    print(*ans[i])