N = int(input())
arr = list(map(int, input().split()))

arr2 = list(sorted(set(arr)))

d = {}
for i in range(len(arr2)):
    d[arr2[i]] = i

ans = []
for i in arr:
    ans.append(d[i])

print(*ans)