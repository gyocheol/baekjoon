import heapq
import sys
input = sys.stdin.readline

N = int(input())

Q = []

for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(Q, (abs(x), x))
    else:
        if Q:
            print(heapq.heappop(Q)[1])
        else:
            print(0)