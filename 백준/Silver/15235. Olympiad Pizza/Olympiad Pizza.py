from collections import deque

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
