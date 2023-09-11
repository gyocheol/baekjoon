ans = []
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            ans.append((i, j))
print(len(set(ans)))