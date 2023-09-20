s = input()
n = len(s)
ans = "z" * n
for i in range(n-2):
    for j in range(i+1, n-1):
        for z in range(j+1, n):
            total = s[:j][::-1]+s[j:z][::-1]+s[z:][::-1]
            if total < ans:
                ans = total
print(ans)