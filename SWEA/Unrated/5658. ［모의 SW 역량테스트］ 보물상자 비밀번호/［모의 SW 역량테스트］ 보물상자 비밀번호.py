T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())
    arr_list = []
    for _ in range(N//4):
        for i in range(0, N, N//4):
            arr_list.append(int(''.join(arr[i:i+N//4]), 16))
        last = arr.pop()
        arr.insert(0, last)
    # print(arr_list)
    all_list = sorted(list(set(arr_list)), reverse=True)
    # print(all_list)
    ans = all_list[K-1]
    print(f'#{t} {ans}')