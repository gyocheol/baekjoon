n = int(input())
ans = 0
ans_list = []
for i in range(n):
    name = input()
    k, m = map(int, input().split())
    total = 0
    while True:
        if k > m:
            break
        m = m + 2 - k
        total += 1
    ans += total
    ans_list.append((total, i, name))
print(ans)
print(sorted(ans_list, key=lambda x:(-x[0], x[1]))[0][2])
