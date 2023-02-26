from collections import deque

N = int(input())
card = deque(i for i in range(1, N+1))
while True:
    if len(card) > 1:
        card.popleft()
    if len(card) > 1:
        p = card.popleft()
        card.append(p)
    if len(card) == 1:
        break
print(*card)