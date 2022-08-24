from collections import deque

def deg(a):
    q = deque()
    for i in range(8):
        q.append(a[i])
    x = 1
    while True:
        if x == 6:
            x = 1

        if q and q[0] - x > 0:
            q.append(q.popleft() - x)
            x += 1
        else:
            q.popleft()
            q.append(0)
            break
    return q


T = 10
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    Q = deg(arr)
    print(f'#{t}', end=' ')
    ans = []
    for i in Q:
        ans.append(i)
    print(*ans)