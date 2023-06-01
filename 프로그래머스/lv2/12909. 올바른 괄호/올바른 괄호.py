def solution(s):
    ans = True
    q = []
    for i in s:
        if not q:
            if i == "(":
                q.append(i)
            else:
                ans = False
        else:
            if i == "(":
                q.append(i)
            else:
                if q[-1] == "(":
                    if i == ")":
                        q.pop()
                    else:
                        ans = False
                else:
                    if i == ")":
                        q.append(i)
    if q:
        ans = False
    return ans