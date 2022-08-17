T = int(input())
for t in range(1, T+1):
    arr = list(map(str, input()))
    print(f'#{t}', end=' ')
    # 패턴의 최대 길이 10
    for i in range(1, 10):
        if arr[:i] == arr[i:i*2]:
            print(i)
            break