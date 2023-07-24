import sys
input = sys.stdin.readline

arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x:(x[1], x[0]))
for i in arr:
    print(*i)