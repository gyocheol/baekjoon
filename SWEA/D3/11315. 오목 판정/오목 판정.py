# 가로, 세로 검사
def solve(a):
    flag = 0
    for i in range(N):
        total = 0
        for j in range(N):
            if a[i][j] == 'o':
                total += 1
            else:
                total = 0
            if total == 5:
                flag = 1
                break
    if flag:
        return 'YES'
    else:
        return 'NO'


# 좌 > 우 대각선 # N이 5이상 이면 오류가 발생
# def solve2(a):
#     total = 0
#     for i in range(N):
#         for j in range(N):
#             if i == j:
#                 if a[i][j] == 'o':
#                     total += 1
#                 else:
#                     total = 0
#     if total == 5:
#         return 'YES'
#     else:
#         return 'NO'

# 좌 > 우 대각선
def solve2(a):
    flag = 0
    for i in range(N-5+1):
        for j in range(N-5+1):
            total = 0
            for z in range(5):
                if a[i+z][j+z] == 'o':
                    total += 1
                else:
                    total = 0
            if total >= 5:
                flag = 1
    if flag:
        return 'YES'
    else:
        return 'NO'

# 우 > 좌 대각선 # N이 5이상 이면 오류가 발생
# def solve3(a):
#     total = 0
#     j = [j for j in range(N-1, -1, -1)]
#     for i in range(N):
#         if a[i][j[i]] == 'o':
#             total += 1
#         else:
#             total = 0
#     if total == 5:
#         return 'YES'
#     else:
#         return 'NO'

# 우 > 좌 대각선
def solve3(a):
    flag = 0
    for i in range(N-5+1):
        for j in range(4, N):
            total = 0
            for z in range(5):
                if a[i+z][j-z] == 'o':
                    total += 1
                else:
                    total = 0
            if total >= 5:
                flag = 1
    if flag:
        return 'YES'
    else:
        return 'NO'


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    arr2 = list(zip(*arr))
    print(f'#{t}', end=' ')
    w = solve(arr)
    h = solve(arr2)
    x = solve2(arr)
    y = solve3(arr)
    l = [w, h, x, y]
    flag = 0
    for i in range(4):
        if l[i] == 'YES':
            flag = 1
        else:
            pass
    if flag == 1:
        print('YES')
    else:
        print('NO')