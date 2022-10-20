import sys
input = sys.stdin.readline

M = int(input())
S = []
for _ in range(M):
    order = input().split()
    if order[0] not in ['all', 'empty']:
        x = int(order.pop())
    if order == ['add']:
        if not S.count(x):
            S.append(x)
    elif order == ['remove']:
        if S.count(x):
            S.remove(x)
    elif order == ['check']:
        if S.count(x):
            print(1)
        else:
            print(0)
    elif order == ['toggle']:
        if S.count(x):
            S.remove(x)
        else:
            S.append(x)
    elif order == ['all']:
        S = [i for i in range(1, 21)]
    elif order == ['empty']:
        S = []