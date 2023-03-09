def solution(participant, completion):
    hash_dict = {}
    sum_hash = 0
    for part in participant:
        hash_dict[hash(part)] = part
        sum_hash += hash(part)

    for comp in completion:
        sum_hash -= hash(comp)

    return hash_dict[sum_hash]