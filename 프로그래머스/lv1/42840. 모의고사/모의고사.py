def solution(answer):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    ans = []
    total = [0, 0, 0]
    for i in range(len(answer)):
        if answer[i] == student1[i%5]:
            total[0] += 1
        if answer[i] == student2[i%8]:
            total[1] += 1
        if answer[i] == student3[i%10]:
            total[2] += 1
    m = max(total)
    for i in range(3):
        if total[i] == m:
            ans.append(i+1)
    
    return ans