T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    la, lb = map(int, input().split())      # a와 b의 길이 받음
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    max_sub = 0

    if la < lb:                             # la가 lb 보다 작을 때
        for i in range(lb-la+1):
            sub = 0
            for j in range(la):
                sub += a[j] * b[i+j]        # 더 긴 숫자열의 i만 움직여 곱함
            if sub > max_sub:
                max_sub = sub

    if la > lb:                             # lb가 la 보다 작을 때
        for i in range(la-lb+1):
            sub = 0
            for j in range(lb):
                sub += b[j] * a[i+j]
            if sub > max_sub:
                max_sub = sub
    print(max_sub)