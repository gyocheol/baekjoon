n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]
students = [[0]*n for _ in range(n)]

for r in range(5):
    for i in range(n):
        for j in range(i+1, n):
            if datas[i][r] == datas[j][r]:
                students[i][j] = 1
                students[j][i] = 1
ans = 1
max_duplication = -1
for i in range(n):
    val = students[i].count(1)
    if val > max_duplication:
        max_duplication = val
        ans = i+1

print(ans)
