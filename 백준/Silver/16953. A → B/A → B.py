from collections import deque

def bfs(a):
    global ans
    q = deque()
    q.append((a, 1))
    # visited[a] = True

    while q:
        x, cnt = q.popleft()

        one = x*2
        if one < B:
            # visited[one] = True
            q.append((one, cnt+1))
        elif one == B:
            ans = cnt+1
            break

        two = int(str(x) + '1')
        if two < B:
            # visited[two] = True
            q.append((two, cnt+1))
        elif two == B:
            ans = cnt+1
            break

A, B = map(int, input().split())
# visited = [False] * (B+1)
ans = -1
bfs(A)
print(ans)