'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
participants = list(map(int, input().split()))
pizza = [0] * n
time = [0] * n
Q = deque(i for i in range(n))
while Q:
    for i in range(len(Q)):
        time[Q[i]] += 1
    q = Q.popleft()
    pizza[q] += 1
    if pizza[q] < participants[q]:
        Q.append(q)

print(*time)
''' # 위는 시간이 오래 걸림 아래는 빼는 방식
import sys
input = sys.stdin.readline
n = int(input())
participants = list(map(int, input().split()))
ans = [0] * n
time = 0
while sum(participants) > 0:
    for i in range(n):
        if participants[i] > 0:
            participants[i] -= 1
            time += 1
            ans[i] = time
print(*ans)