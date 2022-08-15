T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t}', end=' ')
    ans = 1
    for i in range(9):
        # len(set())을 해서 9가 아니면 중복이 있으므로 0을 출력함
        if len(set(arr[i])) != 9:
            ans = 0
            break

        # [arr[j][i] for j in range(len(arr))] row를 한 줄 씩 가지고 옴
        if len(set([arr[j][i] for j in range(len(arr))])) != 9:
            ans = 0
            break

        # i를 0, 3, 6으로 조건을 걸고 j도 0, 3, 6으로 두고 x, y를 더해 l에 append 하고 조건을 검
        if i % 3 == 0:
            for j in range(0, 9, 3):
                l = []
                for x in range(3):
                    for y in range(3):
                        # print(arr[i+x][k+y])
                        l.append(arr[i+x][j+y])
                if len(set(l)) != 9:
                    ans = 0
    print(ans)