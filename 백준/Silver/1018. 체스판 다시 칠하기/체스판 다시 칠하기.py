n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
result = []
for x in range(n-7):
    for y in range(m-7):
        b_start = 0
        w_start = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i + j) % 2:
                    # 체스판 검은색 시작인데 짝수 칸에 W일때
                    if arr[i][j] != "B":
                        b_start += 1
                    # 체스판 흰색 시작인데 짝수 칸에 W일때
                    else:
                        w_start += 1
                else:
                    if arr[i][j] != "W":
                        b_start += 1
                    else:
                        w_start += 1
        result.append(b_start)
        result.append(w_start)
print(min(result))