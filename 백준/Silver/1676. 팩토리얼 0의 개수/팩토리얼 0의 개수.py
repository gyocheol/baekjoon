def f(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


N = int(input())
ans = str(f(N))
total = 0
for i in range(len(ans)-1, -1, -1):
    if ans[i] == '0':
        total += 1
    else:
        break
print(total)