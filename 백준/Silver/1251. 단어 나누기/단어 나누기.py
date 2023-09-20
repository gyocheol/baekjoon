s = input()
n = len(s)
ans = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for z in range(j+1, n):
            total = ""
            total += s[:j][::-1]
            total += s[j:z][::-1]
            total += s[z:][::-1]
            if total not in ans:
                ans.append(total)
ans.sort()
print(ans[0])