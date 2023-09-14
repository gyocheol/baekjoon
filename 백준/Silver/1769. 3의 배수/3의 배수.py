n = input()
num = int(n)
cnt = 0
flag = False
while True:
    total = 0
    if len(str(num)) == 1:
        if not num % 3:
            flag = True
        break
    cnt += 1
    for i in str(num):
        total += int(i)

    if len(str(total)) > 1:
        num = total
    else:
        if not total % 3:
            flag = True
        break

print(cnt)
print("YES" if flag else "NO")