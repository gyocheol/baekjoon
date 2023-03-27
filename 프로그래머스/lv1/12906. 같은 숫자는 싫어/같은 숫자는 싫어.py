def solution(arr):
    answer = []
    n = len(arr)
    for i in range(n):
        if not answer:
            answer.append(arr[i])
        elif answer[-1] == arr[i]:
            pass
        else:
            answer.append(arr[i])
    return answer