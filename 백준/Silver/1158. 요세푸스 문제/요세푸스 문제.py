from collections import deque

n, k = map(int, input().split())

Q = deque()
for i in range(1, n+1):
    Q.append(i)

print("<", end="")
while Q:
    l = len(Q)
    for i in range(k-1):
        Q.append(Q.popleft())
    if l == 1:
        print(Q.popleft(), end="")
    else:
        print(Q.popleft(), end=", ")
print(">")
