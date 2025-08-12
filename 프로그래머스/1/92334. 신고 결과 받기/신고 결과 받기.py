def solution(id_list, report, K):
    n = len(id_list)
    ans = [0] * n
    r_dict = {}
    for item in report:
        u, r = item.split()
        if r not in r_dict:
            r_dict[r] = []
        if u not in r_dict[r]:
            r_dict[r].append(u)
    for k, v in r_dict.items():
        if len(v) >= K:
            for u in v:
                ans[id_list.index(u)] += 1

    return ans