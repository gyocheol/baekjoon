def solution(nums):
    answer = 0
    n = len(nums)
    ans = len(set(nums))
    if ans > n//2:
        answer = n//2
    else:
        answer = ans
    return answer