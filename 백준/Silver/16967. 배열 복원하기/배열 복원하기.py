import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
b_array = [list(map(int, input().split())) for _ in range(h + x)]

for i in range(x, h):
    for j in range(y, w):
        b_array[i][j] -= b_array[i-x][j-y]
for ans in b_array[:h]:
    print(*ans[:w])