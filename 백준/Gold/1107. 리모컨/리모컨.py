'''
101
0
# 1
'''

def solve(n, r, k):
    global min_v
    if k == r:
        if abs(int(''.join(t)) - int(N) + r) >= 0:
            min_v = min(min_v, abs(int(''.join(t)) - int(N)) + r)
            # print(t)

        if 0 < abs(int(''.join(t))) < 100 or abs(int(N)) - 100 > 0:
            min_v = min(min_v, abs(int(N) - 100))

    else:
        for i in range(n):
            t[k] = str(arr[i])
            solve(n, r, k + 1)


N = input()
M = int(input())
arr = [i for i in range(10)]

min_v = 555555

# M이 0이 아닐 때
if M:
    del_list = list(map(int, input().split()))
    for i in del_list:
        arr.remove(i)

    if arr:
        if int(N) == 100:
            print(0)
        else:
            for i in range(max(len(N)-1, 1), min(len(N) + 2, 7)):
                t = [0] * i
                solve(len(arr), i, 0)
            print(min_v)

    # M이 10일때 arr이 다 지워질 때
    else:
        # N이 100보다 크거나 같을 때는 100을 뺌
        if int(N) >= 100:
            print(int(N) - 100)
        # N이 100보다 작을 때
        else:
            print(100 - int(N))


# M이 0일 때
else:
    if int(N) == 100:
        print(0)
    else:
        print(min(len(N), abs(int(N)-100)))