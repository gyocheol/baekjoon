while True:
    n = int(input())
    if n == 0:
        break
    arr = [input().split() for _ in range(n)]
    arr.sort(key=lambda x:x[1], reverse=True)
    ans = arr[0][0]
    for i in range(1, n):
        if arr[i][1] == arr[i-1][1]:
            ans += " " + arr[i][0]
        else:
            break
    print(ans)
