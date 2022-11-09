N = input().split('-')

ans = []

for i in N:
    p = i.split('+')
    total = 0
    for j in p:
        total += int(j)
    ans.append(total)

answer = ans[0]
for i in range(1, len(ans)):
    answer -= ans[i]

print(answer)