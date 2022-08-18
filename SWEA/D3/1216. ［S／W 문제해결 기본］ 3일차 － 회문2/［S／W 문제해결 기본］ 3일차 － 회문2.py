def f(arr):
    M = 100         # 회문 최대 길이
    while M > 1:
        # 행방향
        for i in range(N):
            for j in range(N - M + 1):
                flag = 1
                for k in range(M // 2):
                    if arr[i][j + k] != arr[i][j + M - 1 - k]:
                        flag = 0
                        break
                # 출력
                if flag:
                    return M

        # 열방향
        for i in range(N):
            for j in range(N - M + 1):
                flag = 1
                for k in range(M // 2):
                    if arr[j + k][i] != arr[j + M - 1 - k][i]:
                        flag = 0
                        break
                # 출력
                if flag:
                    return M
        M -= 1


T = 10
for tc in range(1, T + 1):
    N = 100
    no = int(input())
    arr = [list(input()) for _ in range(N)]

    print(f'#{tc}', end=' ')
    print(f(arr))