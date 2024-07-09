import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(int(input())):
    order = list(input().split())
    if order[0] == "1":
        r = int(order[1])-1
        arr[r] = [arr[r][-1]] + arr[r][:-1]
    else:
        arr = list(map(list, zip(*arr[::-1])))
for i in range(n):
    print(*arr[i])
