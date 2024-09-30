def solution(friends, gifts):
    n = len(friends)
    answer = [0] * n
    nums = {}
    for i in range(n):
        nums[friends[i]] = i

    total_all = [[0]*n for _ in range(n)]
    total = [0] * n
    for i in gifts:
        x, y = i.split()
        idxx = nums[x]
        idxy = nums[y]
        total_all[idxx][idxy] += 1
        total[idxx] += 1
        total[idxy] -= 1

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif total_all[i][j] == total_all[j][i]:
                if total[i] > total[j]:
                    answer[i] += 1
            elif total_all[i][j] > total_all[j][i]:
                answer[i] += 1
    
    return max(answer)