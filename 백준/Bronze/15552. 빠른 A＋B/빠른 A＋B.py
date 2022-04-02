import sys
n = int(input())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    print(x+y)
