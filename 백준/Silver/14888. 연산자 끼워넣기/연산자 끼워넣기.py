def dfs(s, total, a, b, c, d):
    global max_ans, min_ans
    if s == N:
        max_ans = max(max_ans, total)
        min_ans = min(min_ans, total)
        return

    if a:
        dfs(s+1, total + arr[s], a-1, b, c, d)
    if b:
        dfs(s+1, total - arr[s], a, b-1, c, d)
    if c:
        dfs(s+1, total * arr[s], a, b, c-1, d)
    if d:
        dfs(s+1, int(total / arr[s]), a, b, c, d-1)
    ## 음수를 양수로 나눌 때는 C++14의 기준 이기 때문에 int로 감싸주고 /를 하나만 써줌


import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))  # +, -, *, /

max_ans = -(10**10)
min_ans = 10**10
# a = +, b = -, c = *, d = /
dfs(1, arr[0], oper[0], oper[1], oper[2], oper[3])

print(max_ans)
print(min_ans)