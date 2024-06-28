T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    while len(arr) > 2:
        arr_h = len(arr)//2
        if len(arr) % 2:        # 홀수
            temp = [0] * (arr_h+1)
            temp[-1] = arr[arr_h]*2
            for i in range(arr_h):
                temp[i] = arr[i]+arr[-i-1]
        else:                   # 짝수
            temp = [0] * arr_h
            for i in range(arr_h):
                temp[i] = arr[i] + arr[-i - 1]
        arr = temp
    print(f'Case #{t+1}: {"Alice" if arr[0] > arr[1] else "Bob"}')
