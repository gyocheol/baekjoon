bracket = input()

ans = 0
tmp = 1
stack = []

for i in range(len(bracket)):
    if bracket[i] == "(":
        tmp *= 2
        stack.append(bracket[i])
    elif bracket[i] == "[":
        tmp *= 3
        stack.append(bracket[i])
    elif bracket[i] == ")":
        if not stack or stack[-1] != "(":
            ans = 0
            break
        if bracket[i-1] == "(": ans += tmp
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] != "[":
            ans = 0
            break
        if bracket[i-1] == "[": ans += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(ans)