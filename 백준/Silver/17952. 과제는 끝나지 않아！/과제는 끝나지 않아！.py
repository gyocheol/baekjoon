import sys
input = sys.stdin.readline

time = int(input())
stack, ans = [], 0
for _ in range(time):
    assignment = list(map(int, input().split()))    # 리스트로 하지 않고 변수명으로 받으면 0이 들어올 때 오류 발생
    if assignment[0] == 1:
        if assignment[2] == 1:
            ans += assignment[1]
        else:
            stack.append([assignment[1], assignment[2]-1])  # 튜플로 하면 stack[-1][1] 여기서 오류발생
    elif stack:
        stack[-1][1] -= 1
        if not stack[-1][1]:
            ans += stack[-1][0]
            stack.pop()
print(ans)