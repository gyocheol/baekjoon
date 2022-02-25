n, m = map(int, input().split())

nums = []
for i in range(m+1):
    for j in range(i):
        if len(nums) == m:
            break
        nums.append(i)
print(sum(nums[n-1:m]))