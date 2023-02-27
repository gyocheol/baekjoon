from collections import deque
import sys
input = sys.stdin.readline

Q = deque()

N = int(input())
n = 0
for _ in range(N):
    arr = input().split()
    if len(arr) > 1:
        n = int(arr[1])
    if arr[0] == "push_front":
        Q.appendleft(n)
    elif arr[0] == "push_back":
        Q.append(n)
    elif arr[0] == "pop_front":
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif arr[0] == "pop_back":
        if Q:
            print(Q.pop())
        else:
            print(-1)
    elif arr[0] == "size":
        print(len(Q))
    elif arr[0] == "empty":
        if len(Q):
            print(0)
        else:
            print(1)
    elif arr[0] == "front":
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif arr[0] == "back":
        if Q:
            print(Q[-1])
        else:
            print(-1)