def f(k):
    global max_v
    # 이동 횟수와 k가 같아지면 max_v를 바꿔줌
    if supple == k:
        if int(''.join(arr)) > max_v:
            max_v = int(''.join(arr))
            # print(max_v)
        return
    # memorization에 있는거면 넘어가기
    if int(''.join(arr)) in memorization:
        # 왜 break와 pass는 오류가 뜨는지..
        return
    # memorization에 v를 추가
    memorization.append(int(''.join(arr)))
    for i in range(N-1):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j], arr[i]
            f(k + 1)
            # 초기화
            arr[i], arr[j] = arr[j], arr[i]


for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    arr, supple = map(int, input().split())
    arr = list(str(arr))
    N = len(arr)
    max_v = 0
    memorization = []
    f(0)
    print(max_v)