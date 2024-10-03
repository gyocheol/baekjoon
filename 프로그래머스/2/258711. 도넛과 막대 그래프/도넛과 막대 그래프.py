def solution(edges):
    ans = [0, 0, 0, 0]
    # 정점 : out 2 이상, in 0
    # 도넛 : 정점 out 간선 - 막대 - 8자
    # 막대 : out 0, in 1 이상
    # 8자 : out 2 이상, in 2 이상
    node = {}
    for a, b in edges:
        if not node.get(a):
            node[a] = [0, 0]    # [0] out
        if not node.get(b):
            node[b] = [0, 0]    # [1] in
            
        node[a][0] += 1
        node[b][1] += 1
    for k, v in node.items():
        if v[0] > 1 and not v[1]:       # 정점
            ans[0] = k
        elif not v[0] and v[1] > 0:    # 막대
            ans[2] += 1
        elif v[0] > 1 and v[1] > 1:     # 8자
            ans[3] += 1
    ans[1] = node[ans[0]][0] - ans[2] - ans[3]
    return ans
