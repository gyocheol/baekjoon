def solve(a):
    dan = -1
    num = []
    for i in range(N-1):
        for j in range(i+1, N):
            num.append(a[i]*a[j])
    for x in range(len(num)):
        n = list(str(num[x]))
        # print(n)
        for _ in range(len(n)-1):
            k = 0
            flag = 1
            while k < len(n)-1:
                if n[k] <= n[k + 1]:
                    k += 1
                else:
                    flag = 0
                    k += 1
                    break

            if flag == 1 and num[x] > dan:
                dan = num[x]
            else:
                break
    return dan


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{t}', end=' ')
    print(solve(arr))