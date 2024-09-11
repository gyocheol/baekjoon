import sys
input = sys.stdin.readline
''' O(N**2) 시간 초과
n = int(input())
check_point = [list(map(int, input().split())) for _ in range(n)]
s_x, s_y = check_point[0][0], check_point[0][1]
ans = 10**4
for i in range(1, n-1):
    x, y = s_x, s_y
    total = 0
    for j in range(1, n):
        if i != j:
            x, y = abs(x - check_point[j][0]), abs(y - check_point[j][1])
            total += x+y
    if total < ans:
        ans = total
print(ans)
'''
n = int(input())
check_point = [list(map(int, input().split())) for _ in range(n)]
ans_list = [0]
for i in range(n-1):
    ans_list.append(abs(check_point[i+1][0] - check_point[i][0]) + abs(check_point[i+1][1] - check_point[i][1]))

ans = sum(ans_list)
min_ans = ans
for i in range(1, n-1):
    distance = ans - (ans_list[i] + ans_list[i+1]) + abs(check_point[i+1][0] - check_point[i-1][0]) + abs(check_point[i+1][1] - check_point[i-1][1])
    min_ans = min(distance, min_ans)
print(min_ans)
