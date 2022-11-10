T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    yy = 0
    xx = 1
    # 반복횟수를 구해서 층과 호수에 사용
    repeat = N//H
    if H < N:
        if N % H:
            yy = N - H*repeat
            xx += N//H
        else:
            yy = H
            xx = N//H
    else:
        yy = N

    if len(str(xx)) > 1:
        print(str(yy) + str(xx))
    else:
        print(str(yy) + '0' + str(xx))