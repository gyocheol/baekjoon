room = input()
ans_list = [0] * 11

for i in room:
    if i == '6' or i == '9':
        if ans_list[6] == ans_list[9]:
            ans_list[6] += 1
        else:
            ans_list[9] += 1
    else:
        ans_list[int(i)] += 1
print(max(ans_list))