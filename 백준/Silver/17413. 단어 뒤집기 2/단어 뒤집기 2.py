S = list(input())
flag = 0
arr = ""
stack = ""
for i in S:
    if i == "<":
        flag = 1
        if stack:
            arr += stack[::-1]
        stack = ""
    elif i == ">":
        arr += stack
        stack = ""
        flag = 0
    if not flag:
        if i == " ":
            arr += stack[::-1] + " "
            stack = ""
        else:
            if i == ">":
                arr += i
            else: stack += i
    else:
        stack += i
if stack:
    if stack[-1] == ">":
        arr += stack
    else:
        arr += stack[::-1]
print(arr)