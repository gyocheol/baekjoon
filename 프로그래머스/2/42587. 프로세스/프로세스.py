from collections import deque

def solution(priorities, location):
    ans = 0
    q = deque([(i, p) for i, p in enumerate(priorities)])
    
    while q:
        idx, p = q.popleft()
        if any(p < max_p for _, max_p in q):
            q.append((idx, p))
        else:
            ans += 1
            if idx == location:
                return ans
