from collections import deque
import sys
input = sys.stdin.readline

arr = deque(i for i in range(1, int(input()) + 1))
ans = []
flag = 1
while arr:
    if len(arr) == 1:
        ans.append(arr[0])
        break
    if flag % 2:
        ans.append(arr.popleft())
    else:
        arr.append(arr.popleft())
    flag += 1
print(*ans)
