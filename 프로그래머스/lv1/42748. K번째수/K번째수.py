def solution(a, c):
    answer = []
    n = len(c)
    for z in range(n):
        i, j, k = c[z][0]-1, c[z][1], c[z][2]-1
        l = a[i:j]
        l.sort()
        answer.append(l[k])
        
    return answer