n, a = map(int, input().split())
x = list(map(int, input().split()))

for i in range(n):
    if x[i] < a:
        print(x[i], end=' ')