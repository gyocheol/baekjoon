def solution(participant, completion):
    hash_dict = {}
    sum_hash = 0
    for p in participant:
        hash_dict[hash(p)] = p
        sum_hash += hash(p)
    for c in completion:
        sum_hash -= hash(c)
    return hash_dict[sum_hash]