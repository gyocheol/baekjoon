import sys
input = sys.stdin.readline

u, n = map(int, input().split())
prices = [0] * 10001
names = [[] for _ in range(10001)]

for i in range(n):
    name, s_price = input().split()
    price = int(s_price)
    prices[price] += 1
    names[price].append(name)

min_val = 10001
min_idx = 10001
for i in range(10001):
    if prices[i] and min_val > prices[i]:
        min_val = prices[i]
        min_idx = i
print(names[min_idx][0], min_idx)