S = list(input()) + [" "]

arr = ""
stack = ""
for i in S:
    if i == ">":
        arr += stack + i
        stack = ""
    elif i == "<" and stack:
        arr += stack[::-1]
        stack = i
    elif i == " " and "<" not in stack:
        arr += stack[::-1] + i
        stack = ""
    else:
        stack += i
print(arr.rstrip())