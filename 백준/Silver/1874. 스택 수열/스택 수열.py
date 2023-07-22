n = int(input())
stack, ans = [], []
flag, cnt = 1, 1

for i in range(n):
    num = int(input())
    while cnt <= num:   # 입력받은 수 까지 append
        stack.append(cnt)
        ans.append("+")
        cnt += 1
    if stack[-1] == num:    # stack의 마지막 수와 num이 같을 땐 pop
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        flag = 0
        break
if flag:
    for i in ans:
        print(i)