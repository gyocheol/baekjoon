for _ in range(int(input())):
    arr = list(map(int, input().split()))
    ans = 0
    n = arr.pop(0)
    for i in range(0, 19):
        for j in range(i+1, 20):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                ans += 1
    print(n, ans)