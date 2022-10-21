N, M = map(int, input().split())
d = {}
for _ in range(N):
    a, b = map(str, input().split())
    d[a] = b

for _ in range(M):
    site = input()
    print(d[site])