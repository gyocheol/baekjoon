def solution(sizes):
    l = []
    r = []
    for i in range(len(sizes)):
        l.append(max(sizes[i]))
        r.append(min(sizes[i]))

    return max(l) * max(r)