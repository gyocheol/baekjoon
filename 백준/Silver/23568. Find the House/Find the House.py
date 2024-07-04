import sys
input = sys.stdin.readline

n = int(input())
d = {}
for _ in range(n):
    i, j, k = input().split()
    i, k = int(i), int(k)
    if j == "L":
        k *= -1
    d[i] = k
start = int(input())

while n:
    n -= 1
    start += d[start]
print(start)