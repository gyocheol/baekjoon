def solution(p, s):
    ans = []
    while p:
        cnt = 0
        while p and p[0] >= 100:
            cnt += 1
            p.pop(0)
            s.pop(0)

        for i in range(len(p)):
            p[i] += s[i]
        if cnt:
            ans.append(cnt)
    return ans