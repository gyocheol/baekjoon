import sys
N = int(sys.stdin.readline())
l = []
for _ in range(N):
    a = int(sys.stdin.readline())
    if a != 0:
        l.append(a)
    else:
        l.pop()
print(sum(l))