dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break
    ans_list = [[0] * C for _ in range(R)]
    arr = [list(input()) for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if arr[x][y] == "*":
                ans_list[x][y] = "*"
                for i in range(8):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != "*":
                        ans_list[nx][ny] += 1
    for i in range(R):
        print("".join(map(str, ans_list[i])))