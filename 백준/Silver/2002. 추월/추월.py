import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
in_car = deque(input() for _ in range(n))
ans = 0
for _ in range(n):
    out = input()
    if in_car[0] == out:
       in_car.popleft()
    else:
        in_car.remove(out)
        ans += 1
print(ans)