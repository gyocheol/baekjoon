n, k = map(int, input().split())
arr = [i for i in range(2, n+1)]
ans, idx, cnt = 0, 0, 0

while cnt < k:
    s = arr[0]
    for i in range(len(arr)):
        x = i-idx
        if not arr[x] % s:
            idx += 1
            cnt += 1
            ans = arr.pop(x)
            if cnt == k:
                break
    idx = 0
print(ans)