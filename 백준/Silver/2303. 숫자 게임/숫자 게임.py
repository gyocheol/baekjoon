from itertools import combinations as comb

n = int(input())
ans, max_first = 0, 0
for i in range(n):
    combi = comb(list(map(int, input().split())), 3)
    temp = 0
    for j in combi:
        temp = max(temp, sum(j) % 10)
    if temp >= max_first and i + 1 > ans:
        ans = i + 1
        max_first = temp
print(ans)
