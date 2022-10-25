N = int(input())

arr = [0]
for _ in range(N):
    arr.append(int(input()))

dp = [0] * (N+1)

if N == 1:
    print(arr[1])
elif N == 2:
    print(arr[1] + arr[2])
else:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    for i in range(3, N+1):
        # arr[i]+dp[i-2] : 자신과 1칸 띄우고 전까지 더해온 것을 더함
        # arr[i]+arr[i-1]+dp[i-3] : 지금까지 더해온 것과 2칸 띄우고 자신과 자신 전을 더함
        dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3])

    print(dp[N])
