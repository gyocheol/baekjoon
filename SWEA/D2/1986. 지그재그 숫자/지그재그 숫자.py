n = int(input())

for i in range(1, n+1):
    ans = 0
    num = int(input())
    for j in range(1, num+1):
        if j % 2 == 1:
            ans += j
        else:
            ans -= j
    print(f'#{i} {ans}')