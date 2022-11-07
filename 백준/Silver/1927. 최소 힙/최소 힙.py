import heapq
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        # heap이 비어있을때
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, n)