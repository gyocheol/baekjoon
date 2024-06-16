n, m = map(int, input().split())
square = [list(input()) for _ in range(n)]

left_up = []
right_down = []

for i in range(n):
    if left_up:
        break
    for j in range(m):
        if square[i][j] == "#":
            left_up = [i, j]
            break
for i in range(n-1, -1, -1):
    if right_down:
        break
    for j in range(m-1, -1, -1):
        if square[i][j] == "#":
            right_down = [i, j]
            break

if square[left_up[0]][(right_down[1]+left_up[1])//2] == ".":
    print("UP")
elif square[right_down[0]][(right_down[1]+left_up[1])//2] == ".":
    print("DOWN")
elif square[(right_down[0]+left_up[0])//2][left_up[1]] == ".":
    print("LEFT")
else:
    print("RIGHT")
