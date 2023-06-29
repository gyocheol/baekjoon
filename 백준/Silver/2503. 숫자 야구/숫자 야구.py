from itertools import permutations

n = int(input())
nums = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))

for _ in range(n):
    test, s, b = map(int, input().split())
    test = list(str(test))
    idx = 0

    for i in range(len(nums)):
        s_cnt, b_cnt = 0, 0
        i -= idx
        for j in range(3):
            test[j] = int(test[j])
            if test[j] in nums[i]:
                if j == nums[i].index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s != s_cnt or b != b_cnt:
            nums.remove(nums[i])
            idx += 1
print(len(nums))