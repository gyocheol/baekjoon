import sys
input = sys.stdin.readline

n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]
ans = []

for i in range(1, 5):
    total = []
    for j in range(n):
        if students[j][0] not in ans:
            total.append([students[j][0], students[j][i]])
    total.sort(key=lambda x:(-x[1], x[0]))
    ans.append(total[0][0])

print(*ans)
