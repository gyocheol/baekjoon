import sys
input = sys.stdin.readline

n = int(input())
stocks = list(map(int, input().split()))
max_v, result = 0, 0

for i in range(n-1, -1, -1):
    max_v = max(max_v, stocks[i])
    result = max(result, max_v-stocks[i])

print(result)
