import sys
input = sys.stdin.readline

t = int(input())
ans_list = [[False] * 100 for _ in range(100)]

for _ in range(t):
    x, y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            ans_list[i][j] = True
ans = 0
for i in ans_list:
    ans += i.count(True)
print(ans)