from collections import deque

def solution(queue1, queue2):
    ans = 0
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    for _ in range(len(q1) * 3):
        if s1 == s2:
            return ans
        if s1 > s2:
            sum_val = q1.popleft()
            s1 -= sum_val
            s2 += sum_val
            q2.append(sum_val)
        elif s1 < s2:
            sum_val = q2.popleft()
            s1 += sum_val
            s2 -= sum_val
            q1.append(sum_val)
        ans += 1
    return -1