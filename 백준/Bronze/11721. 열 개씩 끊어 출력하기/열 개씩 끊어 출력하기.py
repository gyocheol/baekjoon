arr = input()
n = 1
for i in arr:
    if not n % 10:
        print(i, end="\n")
    else:
        print(i, end="")
    n += 1