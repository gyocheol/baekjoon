def solution(clothes):
    d = {}
    n = len(clothes)
    for i in range(n):
        name, cloth = clothes[i][0], clothes[i][1]
        try : d[cloth] += 1
        except : d[cloth] = 1
    ans = 1
    val = list(d.values())
    for i in range(len(val)):
        ans *= (val[i]+1)
    return ans-1