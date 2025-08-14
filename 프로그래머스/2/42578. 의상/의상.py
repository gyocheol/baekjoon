def solution(clothes):
    clothes_dict = {}
    for _, t in clothes:
        if t not in clothes_dict:
            clothes_dict[t] = 2
        else:
            clothes_dict[t] += 1
    ans = 1
    for v in clothes_dict.values():
        ans *= v
    return ans - 1