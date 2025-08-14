def solution(arr):
    ans = []
    for i in arr:
        if ans[-1:] != [i]:
            ans.append(i)
    return ans