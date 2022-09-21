l, r, u, d = [0, -1], [0, 1], [-1, 0], [1, 0]
pipe = [[l, r, d, u], [u, d], [l, r], [u, r], [r, d], [l, d], [l, u]]
for t in range(1, int(input())+1):
    N, M, R, C, L = map(int,input().split())
    visited = [[0] * M for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t}', end=' ')
    # print(arr)
    ans = 1
    Q = [[R, C, 1]]
    visited[R][C] = 1
    while Q:
        row, col, time = Q.pop(0)
        if time == L:
            continue
        p = arr[row][col]-1
        for i in pipe[p]:
            dx = i[0] + row
            dy = i[1] + col
            if 0 <= dx < N and 0 <= dy < M:
                if not visited[dx][dy] and arr[dx][dy] > 0:
                    next_arr = arr[dx][dy] - 1
                    if [-i[0], -i[1]] in pipe[next_arr]:
                        visited[dx][dy] = 1
                        Q.append([dx, dy, time+1])
                        ans += 1
    print(ans)