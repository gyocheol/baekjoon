import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_l, max_c, max_r = arr[0][0], arr[0][1], arr[0][2]
min_l, min_c, min_r = arr[0][0], arr[0][1], arr[0][2]

for i in range(1, N):
    max_l, max_c, max_r = max(max_l, max_c) + arr[i][0], max(max_l, max_c, max_r) + arr[i][1], max(max_c, max_r) + arr[i][2]
    min_l, min_c, min_r = min(min_l, min_c) + arr[i][0], min(min_l, min_c, min_r) + arr[i][1], min(min_c, min_r) + arr[i][2]

print(max(max_l, max_c, max_r), min(min_l, min_c, min_r))