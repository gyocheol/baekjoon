import math
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [True] * (n+1)
arr[0] = arr[1] = False
sqrt_n = int(math.sqrt(n)) + 1

for i in range(2, sqrt_n):
    for j in range(i, n+1, i):
        if i != j:
            if not arr[j]: continue
            arr[j] = False

for i in range(m, n+1):
    if arr[i]:
        print(i)