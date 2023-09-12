import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

rank = 1
if arr[0][0] == k:
    print(rank)
else:
    for i in range(1, n):
        if arr[i][0] == k:
            print(rank)
            break
        total = 1
        if arr[i] == arr[i-1]:
            total += 1
        else:
            rank += 1