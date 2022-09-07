N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]
    for i in range(4, 0, -1):
        if A.count(i) > B.count(i):
            print('A')
            break
        elif A.count(i) < B.count(i):
            print('B')
            break
    else:
        print('D')