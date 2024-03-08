n = int(input())
skills = input()
LR, SK = 0, 0
ans = 0

for skill in skills:
    if skill == "L":
        LR += 1
    elif skill == "R":
        if not LR:
            break
        else:
            LR -= 1
            ans += 1
    elif skill == "S":
        SK += 1
    elif skill == "K":
        if not SK:
            break
        else:
            SK -= 1
            ans += 1
    else:
        ans += 1
print(ans)