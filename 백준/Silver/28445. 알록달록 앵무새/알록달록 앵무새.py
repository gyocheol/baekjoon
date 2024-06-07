parents = []
ans = []
for _ in range(2):
    colors = input().split()
    for color in colors:
        if color not in parents:
            parents.append(color)
for i in range(len(parents)):
    for j in range(len(parents)):
        if [parents[i], parents[j]] not in ans:
            ans.append([parents[i], parents[j]])
ans.sort(key=lambda x:(x[0], x[1]))
for i in range(len(ans)):
    print(" ".join(ans[i]))
