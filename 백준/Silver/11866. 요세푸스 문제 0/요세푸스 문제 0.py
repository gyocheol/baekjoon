from collections import deque

n, k = map(int, input().split())
Q = deque()
for i in range(1, n+1):
    Q.append(i)
ans = []
while Q:
    for i in range(k-1):
        Q.append(Q.popleft())
    ans.append(Q.popleft())

print("<", end="")
for i in range(n):
    if i == n-1:
        print(ans[i], end="")
    else:
        print(ans[i], end=", ")
print(">")