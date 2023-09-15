n = int(input())
arr = [int(input()) for _ in range(n)]
one = arr.pop(0)
ans = 0
if n > 1:
    while True:
        if one <= max(arr):
            one += 1
            arr[arr.index(max(arr))] -= 1
            ans += 1
        else:
            print(ans)
            break
else:
    print(ans)