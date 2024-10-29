import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [[False] * 20 for _ in range(n)]

for _ in range(m):
    a = list(map(int, input().split()))

    if a[0] == 1:
        train[a[1]-1][a[2]-1] = True

    elif a[0] == 2:
        train[a[1]-1][a[2]-1] = False

    elif a[0] == 3:
        for j in range(19, 0, -1):
            train[a[1]-1][j] = train[a[1]-1][j-1]
        train[a[1] - 1][0] = False

    elif a[0] == 4:
        for j in range(19):
            train[a[1]-1][j] = train[a[1]-1][j+1]
        train[a[1]-1][19] = False
ans = 0
passed = []
for i in range(n):
    if train[i] not in passed:
        passed.append(train[i])
        ans += 1
print(ans)
