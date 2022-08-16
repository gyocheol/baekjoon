T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    A, B = map(str, input().split())
    cnt = A.count(B)
    ans = len(A) - (len(B)*cnt)+(1*cnt)
    print(ans)