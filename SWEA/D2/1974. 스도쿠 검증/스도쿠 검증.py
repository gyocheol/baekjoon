T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t}', end=' ')
    flag = 1
    for i in range(9):
        if len(set(arr[i])) != 9:
            flag = 0
        elif len(set(list(zip(*arr))[i])) != 9:
            flag = 0
        if i % 3 == 0:
            for j in range(0, 9, 3):
                l = []
                for x in range(3):
                    for y in range(3):
                        l.append(arr[i+x][j+y])
                if len(set(l)) != 9:
                    flag = 0
    print(flag)