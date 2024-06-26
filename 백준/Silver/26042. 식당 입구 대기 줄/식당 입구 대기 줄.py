import sys
input = sys.stdin.readline
n = int(input())
Q = []
ans = [0, 0]
for _ in range(n):
    info = list(map(int, input().split()))
    if len(info) == 1:
        Q.pop(0)
    else:
        Q.append(info[1])

    if ans[0] < len(Q):
        ans[0] = len(Q)
        ans[1] = Q[-1]
    elif ans[0] == len(Q):
        ans[1] = min(ans[1], Q[-1])

print(ans[0], ans[1])