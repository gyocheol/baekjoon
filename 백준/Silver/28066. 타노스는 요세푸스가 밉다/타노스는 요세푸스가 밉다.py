from collections import deque

n, k = map(int, input().split())
squirrels = deque(range(1, n+1))
while len(squirrels) > k:
    squirrel = squirrels.popleft()
    for _ in range(k-1):
        squirrels.popleft()
    squirrels.append(squirrel)
print(squirrels[0])
