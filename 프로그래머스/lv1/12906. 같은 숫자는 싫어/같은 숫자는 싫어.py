def solution(arr):
    ans = []
    for i in arr:
        if ans[-1:] == [i]: continue
        ans.append(i)
    return ans