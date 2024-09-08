c, r = map(int, input().split())
k = int(input())

if c*r < k:     # 좌석을 줄 수 없는 경우
    print(0)
    exit()

# 4방향
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

seats = [[0]*c for _ in range(r)]
d = x = y = 0
for seat in range(1, c*r+1):
    if seat == k:
        print(y+1, x+1)     # 문제는 [0][r] 부터 시작, 코드는 [0][0]부터 시작! x와 y의 자리를 바꿔줌 
        break
    seats[x][y] = seat
    nx = x+dx[d]
    ny = y+dy[d]
    if nx < 0 or ny < 0 or nx >= r or ny >= c or seats[nx][ny]:
        d = (d+1) % 4
        x += dx[d]
        y += dy[d]
    else:
        x = nx
        y = ny
