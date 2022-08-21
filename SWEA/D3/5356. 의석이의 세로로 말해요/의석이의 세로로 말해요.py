T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    arr = [list(input()) for _ in range(5)]
    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    # print(max_len)
    ans = ''
    for i in range(max_len):
        for j in range(5):
            try: ans += arr[j][i]
            except: pass
    print(ans)