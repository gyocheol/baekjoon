t = int(input())
for _ in range(t):
    ans = 0
    total, idx = map(int, input().split())
    arr = list(enumerate(list(map(int, input().split()))))
    while arr:
        max_v = max([i[1] for i in arr])
        if arr[0][1] == max_v:
            out = arr.pop(0)
            ans += 1
            if out[0] == idx:
                print(ans)
                break
        else:
            back = arr.pop(0)
            arr.append(back)