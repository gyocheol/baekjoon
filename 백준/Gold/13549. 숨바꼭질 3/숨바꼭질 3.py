from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append(n)
    visited = [0] * 100001

    while Q:
        x = Q.popleft()
        if x == m:
            return visited[x]
        for i in [x*2, x-1, x+1]:
            if 0 <= i < 100001 and not visited[i]:
                if i == x*2:
                    visited[i] = visited[x]
                    Q.append(i)
                else:
                    visited[i] = visited[x] + 1
                    Q.append(i)


n, m = map(int, input().split())
print(bfs())