import sys
input = sys.stdin.readline

S = []
n = int(input())
for _ in range(n):
    order = input().split()
    if order[0] not in ["all", "empty"]:
        x = int(order.pop())
    if order[0] == "add":
        if not S.count(x):
            S.append(x)
    elif order[0] == "remove":
        if S.count(x):
            S.remove(x)
    elif order[0] == "check":
        if S.count(x):
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        if S.count(x):
            S.remove(x)
        else:
            S.append(x)
    elif order[0] == "all":
        S = [i for i in range(1, 21)]
    elif order[0] == "empty":
        S = []
