n = int(input())

i = n
while i:
    for j in range(1, n*2, 2):
        i -= 1
        print(" " * i + "*" * j)

x = 1
while x:
    if x > n - 1:
        break
    for j in range(n*2-3, 0, -2):
        print(" " * x + "*" * j)
        x += 1