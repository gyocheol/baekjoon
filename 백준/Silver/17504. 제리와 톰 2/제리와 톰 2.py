# 수학
n = int(input())
cheese = list(map(int, input().split()))[::-1]
up, down = 1, cheese[0]     # up / down

for c in cheese[1:]:
    up, down = down, c * down + up
print(down-up, down)