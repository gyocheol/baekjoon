N = int(input())
for _ in range(N):
    arr = input()
    l = []
    flag = 1
    for i in arr:
        if i == '(':
            l.append(i)
        else:
            if l:
                l.pop()
            else:
                flag = 0
    if l:
        flag = 0

    if flag:
        print('YES')
    else:
        print('NO')